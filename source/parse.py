#!/usr/bin/python

import requests
import sys
import getopt
from io import StringIO

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def main(argv):
    #generate urls
    userName = 'CommandCast'
    pages = 1
    verbose = False
    try:
        opts, args = getopt.getopt(argv,"hp:u:v:",["pages=","user=", "verbose="])
    except getopt.GetoptError:
        print("parse.py -p <pages> -u <user> -v <verbose>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("parse.py -p <pages> -u <user> -v <verbose>")
            sys.exit()
        elif opt in ("-p", "--pages"):
            pages = int(arg)
        elif opt in ("-u", "--user"):
            userName = arg
        elif opt in ("-v", "--verbose"):
            verbose = str2bool(arg)
    if pages < 1 or pages > 20 or not userName:
        print ("Usage: parse.py -p <pages> -u <user> -v <verbose>")
        sys.exit()

    # This is the main code.  Everything above this is just parsing user input.
    decks = []
    for page in range(1, pages+1):
        try:
            # generate link for the user's first page.  if the script breaks, turn on verbose mode and verify this page loads.
            pageUri = "https://tappedout.net/users/{1}/mtg-decks/?&p={0}&page={0}".format(page, userName)
            if verbose:
                print(pageUri)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
            r = requests.Session()
            response = r.get(pageUri, headers=headers)
            body = response.content.decode()
            # split the page contents by double quote as all URIs in the page will be quoted
            items = body.split("\"")
            for parsedItem in range(0, len(items)):
                item = items[parsedItem]
                # each deck link for a user will contain "mtg-decks/.  We found a deck link
                if "mtg-decks/" in item:
                    decks.append(item)
            if verbose:
                print("Downloaded and parsed page {0}".format(page))
        except:
            print("Unexpected error:", sys.exc_info()[0])
    # because we overcollected deck links, use the list(set()) function to generate unique decks
    uniqueDecks = list(set(decks))
    # clear out broken links which also include mtg-decks
    uniqueDecks.remove("/mtg-decks/search/")
    uniqueDecks.remove("/accounts/login/?next=/users/{0}/mtg-decks/".format(userName))
    uniqueDecks.remove("/accounts/register/?next=/users/{0}/mtg-decks/".format(userName))

    cards=[]
    # now we've filtered for unique decks for the user.  let's parse them individually
    for deck in range(0, len(uniqueDecks)):
        try:
            pageUri = "https://tappedout.net{0}".format(uniqueDecks[deck])
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
            r = requests.Session()
            response = r.get(pageUri, headers=headers)
            body = response.content.decode()
            #verify it's an EDH deck
            if "/mtg-deck-builder/edh/" in body:
                # each affiliate link uses hidden inputs.  Here we find the first affiliate link on the page
                garbage = body.split("<input type=\"hidden\" name=\"c\" value=\"")
                # take the text after the affiliate link but before the next end quote (the first split) and then split the
                # cards by ||.  If the script breaks, it's most likely this code.  View page source on TappedOut and find the new
                # way they generate affiliate links.  Update parsing logic.
                deckCards = garbage[1].split("\"")[0].split("||")
                cards= cards + deckCards
                if verbose:
                    print("Parsed deck {0}".format(uniqueDecks[deck]))
        except:
            print("Unexpected error:", sys.exc_info()[0])
    if verbose:
        print("Parsed {0} decks and found {1} cards".format(len(uniqueDecks), len(cards)))
    totals = {}
    # Now that we've parsed all the decks and found all the cards, clean and aggregate
    for card in range(0, len(cards)):
        try:
            if "1 " in cards[card]:
                cardName = cards[card].split("1 ")[1]
            # Because we're parsing HTML, they've used HTML codes for single quote.  Clean them up.
            cardName = cardName.replace("&#39;", "'")
            if cardName:
                if cardName in totals:
                    totals[cardName] = totals[cardName] + 1
                else:
                    totals[cardName] = 1
        except:
            print("Error parsing card {0}".format(cardName))
            print(sys.exc_info()[0])
    # print aggregated results
    for key, value in totals.items():
        print("{0},{1}".format(value, key))

if __name__ == "__main__":
   main(sys.argv[1:])
