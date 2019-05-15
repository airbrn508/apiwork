#!/usr/bin/env python3

import requests
import webbrowser as wb
from pprint import pprint

'''
https://api.spacexdata.com/v3/launches/latest

- telemetry stuff
- display name of mission (mission name)
- launch date
- 1 other piece of info you think is critical or interesting
- tell the users, "PRESS ENTER TO ACCESS..."
  - dealer's choice to open ONE link provide by response

code to open link:
import webbrowser
webbrowser.open('http://www.nasa.gov')

'''

API_URL = "https://api.spacexdata.com/v3/launches/latest"

spacex = requests.get(API_URL)
spacex = spacex.json()

launchdate = spacex['launch_date_local']
missionname = spacex['mission_name']
rocketname = spacex['rocket']['rocket_name']

#pprint(spacex)

print()
print(missionname)
print(launchdate)
print(rocketname)

input("PRESS ENTER TO ACCESS: ")
wb.open(spacex['links']['video_link'], new=True)

