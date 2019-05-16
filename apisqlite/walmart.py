#!/usr/bin/env python3
"""Price tracker & comparison shop tool"""

import requests
import sqlite3
import time
from pprint import pprint

WUPC = "http://api.walmartlabs.com/v1/items?"
APIKEY = "apiKey=d7hjdvye4sky5cdwmmmtf3bf"

def upclookup(wupc):
    resp = requests.get(WUPC + APIKEY + wupc)
    if resp.status_code == 200:
        return resp.json()
    else:
        return False

def trackmeplease(tracktime, trackprice):
    conn = sqlite3.connect('price.db')
    try:
        conn.execute('''CREATE TABLE PRICE
        (TIME VARCHAR2 PRIMARY KEY     NOT NULL,
        PRICE REAL  NOT NULL);''')
    except:
        pass

    conn.execute("INSERT INTO PRICE (TIME, PRICE) VALUES (?, ?)",(tracktime, trackprice))
    conn.commit()

    cursor = conn.execute("SELECT TIME, PRICE FROM PRICE")
    for row in cursor:
        print("TIME:", row[0])
        print("PRICE:", row[1])

    print("Database operation done")
    conn.close()
    return


def main():
    #wupc = input("What is the UPC you wish to lookup? ")
    wupc = '190198511270'
    wupc = "&upc=" + wupc

    respjson = upclookup(wupc)

    if respjson:
        print(respjson['items'][0]['name'])
        print(respjson['items'][0]['salePrice'])
        print((respjson['items'][0]['shortDescription']).replace("&rsquo;", "'"))
        print("\nShould we track this data within the database?")
        if input("y/n: ").lower() == 'y':
            print(time.ctime())
            trackmeplease(time.ctime(), respjson['items'][0]['salePrice'])
        else:
            print("\nThanks for checking prices!")
    else:
        print("\nThe UPC lookup failed.")

if __name__ == "__main__":
    main()

