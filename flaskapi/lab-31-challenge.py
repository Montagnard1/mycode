#!/usr/bin/python3
"""
Challenge for Flask lab 31
Use the requests module to send a GET
"""
import requests

n = 52
while(n > 0):
    x = requests.get("http://10.7.97.3:2224/fast").text
    n -= 1
    print(x)

