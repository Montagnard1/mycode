#!/usr/bin/python3
''' Challenge at https://github.com/csfeeser/Python/blob/master/challenges/API%20CHALLENGE%20INTO-%20ISS.md
 Access this URL with requests:
 http://api.open-notify.org/iss-now.json
'''

import sys
import requests
from pprint import pprint

# main function
def main(args):
    ## Define NEOW URL
    NEOURL = "http://api.open-notify.org/iss-now.json"

    # make a request with the request library
    response = requests.get(NEOURL).json()
    # pprint(response)
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Lon: {response['iss_position']['longitude']}")
    print(f"Lat: {response['iss_position']['latitude']}")

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
