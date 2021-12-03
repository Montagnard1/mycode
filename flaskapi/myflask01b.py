#!/usr/bin/python3  
import sys
import datetime
import requests
from pprint import pprint

# main function
def main(args):
    ## Define NEOW URL
    # NEOURL = "http://10.7.97.3:2224/"

    # make a request with the request library
    # response = requests.get(NEOURL).json()
    r= requests.get("http://10.7.97.3:2224/slappy").text
    print(r)
    

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
