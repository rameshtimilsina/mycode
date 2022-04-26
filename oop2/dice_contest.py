#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()
    #the player known as 3ormore_dice
    threeormore_dice = Cheat_RollOneMore_lessthan3()
    # track scores for both players
    swapper_score = 0
    loaded_dice_score = 0
    threeormore_dice_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        threeormore_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()
        threeormore_dice.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) == sum(threeormore_dice.get_dice()):
            print("Draw!")
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(threeormore_dice.get_dice()):
            print("Dice swapper wins!")
            swapper_score+= 1
        elif sum(threeormore_dice.get_dice()) > sum(swapper.get_dice()) and sum(threeormore_dice.get(dice())) > sum(loaded_dice.get_dice()):
            threeormore_dice_score+=1

        else:
            print("Loaded dice wins!")
            loaded_dice_score += 1
        

        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"3 or more score dice won: {threeormore_dice_score}")
    # determine the winner
    if swapper_score == loaded_dice_score == threeormore_dice_score:
        print("Game was drawn")
    #elif swapper_score > loaded_dice_score and swapper_score > threeormore_dice_score:
    #    print("Swapper won most games")
    
    #elif threeormore_dice_score > swapper_score and threeormore_dice_score > loaded_dice_score:
    #    print ("3 or more score cheater won most games")
    #else:
    #    print("Loaded dice won most games")
    maxscoreby=max(swapper_score,loaded_dice_score,threeormore_dice_score)
    if maxscoreby == swapper_score:
        print("Swapper cheater won!!")
    elif maxscoreby==loaded_dice_score:
        print("Loaded dice cheater won!!")
    else:
        print("Three or More score cheater won!!")


if __name__ == "__main__":
    main()

