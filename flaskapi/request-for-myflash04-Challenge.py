#!/usr/bin/python3
"""
Challenge for Flask challenge part 2 on day 4.
Use the requests module to send a POST
"""
import requests
url = "http://10.7.97.3:2224/post"

ben_dict = {
    "nm" : "42"
}

requests.post(url, json = ben_dict)

