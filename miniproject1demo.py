#!/usr/bin/env python3
"""Guess the Number Game"""

import random # standard library, tools that ship with Python

### GOALS:
# generate a random number
# user will make a guess
# user's guess will be compared to the random number
# if the guess was too high or too low, let the user know that
# if the guess is correct, the game should end

### STRETCH GOAL:
# if they are CLOSE, let them know that
# handle if the user types in something that isn't a number

num= random.randint(1, 100)

# if they type in something other than a number,
# this will error!

round= 0

print("DEBUG:", num)

while round < 5:
    guess= input("Select a number between 1 and 100\n>")
    guess= int(guess)

    # check if guess is too high
    if guess > num:
        print("Your number is too high!")
        round += 1

    # check if guess is too low
    elif guess < num:
        print("Your number is too low!")
        round += 1

    else:
        print("You are correct! The answer was", num)
        break

    if round < 5:
         print("Guess again!")





