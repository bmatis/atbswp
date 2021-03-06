#!/usr/bin/env python3
# lucky.py - Opens several google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
searchTerms = ' '.join(sys.argv[1:])
res = requests.get('http://google.com/search?q=' + searchTerms)
res.raise_for_status()

# Retrieve top search result links.
googleSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = googleSoup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
