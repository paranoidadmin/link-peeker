#!/usr/bin/env python3
"""
Name: lp.py | link-peeker.py
Description: Grab the "real" link behind the shortened link for Supported
             shorteners.
"""
import argparse
import requests


"""
Configuration:
"""
#Supported shortening services, stored in array.
services = ["tinyurl", "bitly", "bit.ly", "buff.ly"]


"""
Function Name: get_link
Description: grab the long url and return it as llink
"""
def get_link(link):
    r = requests.get(link)
    # long link
    llink = r.request.url
    return llink

"""
Build out arguments and assign variables
"""
parser = argparse.ArgumentParser(description='Reveal hidden links behind shortend URLS')
parser.add_argument('link', help="The link you want to grow")
args = parser.parse_args()

link = args.link

"""
App Logic
"""
if any(x in link for x in services):
    llink = get_link(link)
    print('The long link is: ' + llink)
else:
    print("I'm not able to handle this URL: " + link)
    print("Sorry about it")
