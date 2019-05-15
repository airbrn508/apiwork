#!/usr/bin/env python3
"""learning about NEO from NASA | chris.marquardt2@vzw.com"""

import requests
from pprint import pprint
from datetime import datetime


## define api_key (read in from file)
with open("neo.key") as neokey:
    api_key = neokey.read()

## lookup nasa api
## GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY
start_date = datetime.today().strftime('%Y-%m-%d')
end_date = start_date

bigrocks = requests.get(r"https://api.nasa.gov/neo/rest/v1/feed?start_date="+start_date+"&end_date="+end_date+"&api_key="+api_key)

neo = bigrocks.json()

counter = 0
for x in neo['near_earth_objects']:
    for y in neo['near_earth_objects'][x]:
        if y['is_potentially_hazardous_asteroid'] is True:
            print(y['name'], y['close_approach_data'][0]['close_approach_date'], "\n\n")
            counter += 1
            pprint(y)

if counter > 0:
    print("Prepare for impact!")
else:
    print("No threat of impact !!!")
    print("Today is a good day")

