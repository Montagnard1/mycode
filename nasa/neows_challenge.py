#!/usr/bin/python3
"""
Challenge to Lab 20:
. query the user for a start and end date
. return how many asteroids were present in that range
. return how many asteroids were potentially hazardous in that range
. Stretch Goal: In terms of kms, what was the biggest asteroid in that range? The fastest? The closest?
"""
import requests
from pprint import pprint

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def get_date(message):
    date = input(message)
    return date

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    # get the start date
    startdate = get_date("Please specify the start date : ")
    startdate = f"start_date={startdate}"
    # get the end date
    enddate = get_date("Please specify the end date : ")
    enddate = f"end_date={enddate}"
    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)
    # extract the json attachment from our response
    neodata = neowrequest.json()
    # See how many how  asteroids were present in that range
    print(f"Asteroids present in that range : {neodata['element_count']}")
    # See how many are hazardous, the biggest, fastest and closest
    number_of_hazardous_objects = 0
    size = 0
    speed = 0
    miss_d = 9999999999999999
    for date_x in neodata["near_earth_objects"].keys():
        i = 0
        for obj in neodata["near_earth_objects"][date_x]:
            # print(neodata["near_earth_objects"][date_x][i]["name"])
            if neodata["near_earth_objects"][date_x][i]["is_potentially_hazardous_asteroid"] == True:
                print(f"{neodata['near_earth_objects'][date_x][i]['name']} is potentially dangerous!")
                number_of_hazardous_objects += 1
            # Look at the max diameter
            max_diameter = neodata['near_earth_objects'][date_x][i]['estimated_diameter']["kilometers"]["estimated_diameter_max"]
            if max_diameter > size:
                size = max_diameter
            # Look at the fastest speed
            max_speed = neodata['near_earth_objects'][date_x][i]['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
            if float(max_speed) > float(speed):
                speed = max_speed
            # Look at the closest
            miss_dist = neodata['near_earth_objects'][date_x][i]['close_approach_data'][0]['miss_distance']['lunar']
            if float(miss_dist) < float(miss_d):
                miss_d = miss_dist
            i += 1
    print(f"Number of hazardous asteroids : {number_of_hazardous_objects}")
    print(f"Maximum diameter (kms) : {size}")
    print(f"Maximum speed (km/second): {speed}")
    print(f"Closest miss distance (lunar): {miss_d}")

if __name__ == "__main__":
    main()
