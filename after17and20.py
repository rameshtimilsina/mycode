#!/usr/bin/env python3

pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

choice= input("Name a Generation 1 starter Pokemon:\n>")

if choice == pokedex[key]:
    print ("Success")
else:
    print ("Failed")
#    print(pokedex[choice])
#else:
#    print("Sorry, we don't have any record of that Pokemon!")

