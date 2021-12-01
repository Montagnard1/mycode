#!/usr/bin/python3
"""This is the code customization done by Benoit Legault for the Lab 19 of the
   API & API design course:
   CODE CUSTOMIZATION 01 - Return the house(s) affiliated with the character looked up
   along with a list of books they appear in.

   Alta3 Research - Exploring OpenAPIs with requests
"""

# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response
    got_dj = gotresp.json()
    # Get the house(s) affiliated with the character
    print(f"Character: {got_dj['name']}")
    print("House(s) affiliated with the character:")
    for allegiance in got_dj["allegiances"]:
        house = requests.get(allegiance).json()['name']
        print(f"\t{house}")
    # Get the book(s) in which the character appears
    print("Books(s) in which the character appears :")
    for bk in got_dj["books"]:
        book_name = requests.get(bk).json()['name']
        print(f"\t{book_name}")
    for bk in got_dj["povBooks"]:
        book_name = requests.get(bk).json()['name']
        print(f"\t{book_name}")

if __name__ == "__main__":
    main()
