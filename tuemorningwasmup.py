#!/usr/bin/env python3

import requests

url ="https://anapioficeandfire.com/api/characters/12"

slicename=requests.get(url).json()

#print out this characters name
print(slicename['name'])


#print out this characters actor
print(slicename['playedBy'][0])
#print out all of this characters aliases

