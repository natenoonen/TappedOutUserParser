#!/usr/bin/python

import pycurl
import sys
from StringIO import StringIO

#generate urls
#TODO: Maybe make this generic?
pages = 3
userName = "CommandCast"
decks = []
for page in range(1, pages+1):
    pageUri = "http://tappedout.net/users/{1}/mtg-decks/?&p={0}&page={0}".format(page, userName)
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
        print("Parsed deck {0}".format(uniqueDecks[deck]))
    except:
        print("Unexpected error:", sys.exc_info()[0])
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
    print("{0} {1}".format(value, key))
