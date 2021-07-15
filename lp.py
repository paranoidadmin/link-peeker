#!/usr/bin/env python3

import argparse
import requests

"""
Build our Args
"""
parser = argparse.ArgumentParser(description='Reveal hidden links behind shortend URLS')
parser.add_argument('link', help="The link you want to grow")
args = parser.parse_args()

def get_link(link):
    r = requests.get(link)
    # long link
    llink = r.request.url
    print('The long link is: ' + llink)

link = args.link

#supported services
services = ["tinurl", "bitly", "bit.ly"]

if any(x in services for x in services):
    get_link(link)
else:
    print("I'm not able to handle this URL: " + link)
