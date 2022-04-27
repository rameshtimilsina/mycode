#!/usr/bin/env python3

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

#    print(pokeapi)
    #print url for the image
    print(f"The URL to the image of {pokeapi['species']['name']} is \{pokeapi['sprites']['front_default']}")
    imgurl=pokeapi['sprites']['front_default']
    wget.download(imgurl, "/home/student/static/")


    #print all the moves
    moveslist = pokeapi.get('moves')
    #print (moveslist)
    for x in moveslist:
        print('>>>> ',x['move']['name'])
    #print how many time has the pokemon appeared
    countforappearance=len(pokeapi.get('game_indices'))
    print (f"\n{(pokeapi['species']['name']).capitalize()} has appeared in {countforappearance} games!!")

main()

