#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"
URLnew= "http://api.open-notify.org/iss-now.json"
def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()
    slicemenew=requests.get(URLnew).json()
    #print(sliceme)
    #print(type(sliceme))

    print(f"people in space: {sliceme['number']}")
    for i in sliceme['people']:
        print(f"{i['name']} is on the {i['craft']}")

    print ("\nCURRENT LOCATION OF THE ISS:")
    #for x in slicemenew['iss_position']:
    print(f"Lon: {slicemenew['iss_position']['longitude']}")
    print(f"Lat: {slicemenew['iss_position']['latitude']}")
main()
