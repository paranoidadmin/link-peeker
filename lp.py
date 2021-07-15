#!/usr/bin/env python3

import argparse
import requests

"""
Build our Args
"""
parser = argparse.ArgumentParser(description='Reveal hidden links behind shortend URLS')
parser.add_argument('link', help="The link you want to grow")
args = parser.parse_args()

# TinyURL = https://tinyurl.com/8k467rsz
link = args.link
if "tinyurl" in link:
    #mode=tu #TinyURL
    r = requests.get(link)
    print('The long link is: ' + r.request.url)
else:
    print("I'm not able to handle this URL: " + link)
