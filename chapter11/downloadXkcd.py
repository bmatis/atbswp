#!/usr/bin/env python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4, logging
logging.basicConfig(level=logging.INFO,
    format=' %(asctime)s - %(levelname)s - %(message)s')

url = 'http://www.xkcd.com/50/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page
    logging.info('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        logging.warn('Could not find comic image for: %s.' % (url))
    else:
        comicURL = 'http:' + comicElem[0].get('src')

        # Download the image.
        logging.info('Downloading image %s...' % (comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://www.xkcd.com' + prevLink.get('href')

print('Done.')