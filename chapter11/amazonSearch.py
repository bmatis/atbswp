#!/usr/bin/env python3
# amazonSearch.py - Opens several amazon search results.

import requests, sys, webbrowser, bs4
import logging
logging.basicConfig(level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s')

# Provide feedback to user that search has started
print('Searching Amazon now...')

# Get the search terms from command line and put into single string
searchTerms = ' '.join(sys.argv[1:])

# Make a header so script looks like a browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15'}

# Request the results from Amazon
res = requests.get('https://www.amazon.com/s/?field-keywords=' + searchTerms,
    headers=headers)
res.raise_for_status()

# Retrieve the search result links.
amazonSoup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = amazonSoup.select('a.s-access-detail-page')

# Open browser tab for each result.
numOpen = min(5, len(linkElems))
print('Opening %s results...' % (numOpen))
for i in range(numOpen):
    link = linkElems[i].get('href')

    # some of the links are relative, so add domain if missing
    if link.startswith('http'):
        pass
    else:
        link = 'https://www.amazon.com' + link
    logging.info('Opening: ' + link)

    webbrowser.open(link)