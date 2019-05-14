#!/usr/bin/python3
"""Openstack json parsing
author: chris.marquardt2@verizonwirelss.com
learning about json and python
"""

import json

def main():
    """runtime code"""
#   with open(r'C:\Users\marqch1\PycharmProjects\verizon0513\venv\openstackresponse01.json', 'r') as openjson:
    with open('openstackresponse01.json', 'r') as jsonfp:
        jsondecoded = json.load(jsonfp)
        print(jsondecoded['server']['imageRef'])


main()
