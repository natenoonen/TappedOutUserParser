#!/usr/bin/python

import pycurl
import re
from StringIO import StringIO

#generate urls
#TODO: Maybe make this generic?
pages = 1
decks = []
for page in range(1, pages+1):
    pageUri = "http://tappedout.net/users/commandersbrew/mtg-decks/?&p={0}&page={0}".format(page)
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
uniqueDecks.remove("/accounts/login/?next=/users/commandersbrew/mtg-decks/")
uniqueDecks.remove("/accounts/register/?next=/users/commandersbrew/mtg-decks/")

cards=[]
for deck in range(0, len(uniqueDecks)):
    pageUri = "http://tappedout.net{0}".format(uniqueDecks[deck])
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, pageUri)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    garbage = body.split("http://store.tcgplayer.com/massentry?partner=TPPDOUT&amp;c=")
    deckCards = garbage[1].split("\"")[0].split("||")
    cards= cards + deckCards
    print("Parsed deck {0}".format(uniqueDecks[deck]))
print("Parsed {0} decks and found {1} cards".format(len(uniqueDecks), len(cards)))

#TODO: Aggregate
