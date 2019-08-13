#!/usr/bin/env python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, pprint
API_KEY = '9f107ac810c12956a288e28029f94cb1'


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickweather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

print("Getting weather for: " + location)

# Download the JSON data from OpenWeatherMaps.org's API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (location, API_KEY)
print(url)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
#pprint.pprint(weatherData)

# Print weather descriptions.
print('Current weather in %s:' % (location))
print(weatherData['weather'][0]['main'], '-', weatherData['weather'][0]['description'])
kelvinTemp = weatherData['main']['temp']
print('Temp in Kelvin is:', kelvinTemp)
fTemp = 1.8 * (kelvinTemp-273) + 32
print('Temp in F is:', round(fTemp,2))

