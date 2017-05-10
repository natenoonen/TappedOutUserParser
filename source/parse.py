#!/usr/bin/python

import pycurl
import sys
import getopt
from StringIO import StringIO

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
        print 'parse.py -p <pages> -u <user> -v <verbose>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'parse.py -p <pages> -u <user> -v <verbose>'
            sys.exit()
        elif opt in ("-p", "--pages"):
            pages = int(arg)
        elif opt in ("-u", "--user"):
            userName = arg
        elif opt in ("-v", "--verbose"):
            verbose = str2bool(arg)
    if pages < 1 or pages > 20 or not userName:
        print 'Usage: parse.py -p <pages> -u <user> -v <verbose>'
        sys.exit()
    decks = []
    for page in range(1, pages+1):
        pageUri = "http://tappedout.net/users/{1}/mtg-decks/?&p={0}&page={0}".format(page, userName)
        if verbose:
            print(pageUri)
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, pageUri)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        items = body.split("\"")
        for parsedItem in range(0, len(items)):
            item = items[parsedItem]
            if "mtg-decks/" in item:
                decks.append(item)
        if verbose:
            print("Downloaded and parsed page {0}".format(page))
    uniqueDecks = list(set(decks))
    uniqueDecks.remove("/mtg-decks/search/")
    uniqueDecks.remove("/accounts/login/?next=/users/{0}/mtg-decks/".format(userName))
    uniqueDecks.remove("/accounts/register/?next=/users/{0}/mtg-decks/".format(userName))

    cards=[]
    for deck in range(0, len(uniqueDecks)):
        try:
            pageUri = "http://tappedout.net{0}".format(uniqueDecks[deck])
            buffer = StringIO()
            c = pycurl.Curl()
            c.setopt(c.URL, pageUri)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            c.close()
            body = buffer.getvalue()
            garbage = body.split("<input type=\"hidden\" name=\"c\" value=\"")
            deckCards = garbage[1].split("\"")[0].split("||")
            cards= cards + deckCards
            if verbose:
                print("Parsed deck {0}".format(uniqueDecks[deck]))
        except:
            print("Unexpected error:", sys.exc_info()[0])
    if verbose:
        print("Parsed {0} decks and found {1} cards".format(len(uniqueDecks), len(cards)))
    totals = {}
    for card in range(0, len(cards)):
        cardName = cards[card].split("1 ")[1]
        cardName = cardName.replace("&#39;", "'")
        if cardName in totals:
            totals[cardName] = totals[cardName] + 1
        else:
            totals[cardName] = 1

    for key, value in totals.items():
        print("{0},{1}".format(value, key))

if __name__ == "__main__":
   main(sys.argv[1:])
