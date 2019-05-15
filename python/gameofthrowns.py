#!/usr/bin/env python3

import requests
from pprint import pprint

bookno = input("Which book are you searching on (1-5)?")
bookurl = "https://www.anapioficeandfire.com/api/books/"+bookno

book = requests.get(bookurl)
book = book.json()


print("That book is:", book['name'])


with open(((book['name']).replace(' ', ''))+".txt", "w") as bookout:
    for charlink in book['characters']:
        character = requests.get(charlink)
        character = character.json()
        if character['name'] != '':
            print(character['name'], file=bookout)

print("We are done!")
