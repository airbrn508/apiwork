#!/usr/bin/env python3
"""VzW | Christopher J Marquardt"""

import requests
import pprint

LOOKUPAPI = r"http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=17042&date=2019-05-14&\distance=25&API_KEY=EE908C02-A593-45DB-A595-16144A250B63"

def main():
    r = requests.get(LOOKUPAPI)
    pp = pprint.PrettyPrinter(indent=4)
#   pp.pprint(r.json())

    evenlist = (r.json())[0::2]
    for day in evenlist:
        print(day['DateForecast'])
        print(day['ReportingArea'], day['StateCode'], sep=", ")
        print("Today's air quality is:", day['Category']['Name'])
        print(day['Discussion'])
        print()
        input("-- Press Enter to Continue --")
        print()




main()
