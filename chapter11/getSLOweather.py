#!/usr/bin/env python3

import bs4, requests

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=35.2796&lon=-120.6611#.Wxbk8C2ZOL8')
res.raise_for_status()

weatherSoup = bs4.BeautifulSoup(res.text, 'html.parser')
temp = weatherSoup.select('.myforecast-current-lrg')[0]
print(temp.getText())