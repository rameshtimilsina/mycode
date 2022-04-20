#!/usr/bin/env python3

name = str(input("Enter your name. "))
print(f"Hello there {name.capitalize()}. Welcome to the world of choices. Your survival depends on your choices in this world.")
play=int(input("If you want to continue this journey press 1, press 2 if you are a scaredycat and want to quit: "))
if play==2:
    print("Not much of an adventurer, are we?")
elif play==1:
    print("I see you are an adventurer. Let's begin.")
    print("You are crossing the road and you see a speeding car coming towards you \n What do you want to do: 1. Stop in the middle of the road. 2. Run to cross the road")
    choice1=int(input("Press 1 or 2 "))
    if choice1==1:
        print ("That's a weird choice. I guess you chose death")
    elif choice1==2:
        print ("You barely survived")
        print("Well now you are safe and walking on the sidewalk. You see a person running towards you with a knife. \n  What do you do? 1. Charge towards the person 2. Accept your fate and stay frozen")
        choice2=int(input("Press 1 or 2 "))
        if choice2==1:
            print("Well, that was not an intelligent choice. Your bare hands are no match for a knife. You are dead.")
        elif choice2==2:
            print("Takes some strength to accept your fate. The person charged at you with a knife and gutted you. You are no longer of this planet. So long")
        else:
            print("I get reading is hard. No choice means death in this world. YOU ARE DEAD.") 
    else:
        print("Bad decisions led to death. YOU ARE DEAD.")
else:
    print ("You must be bad at reading. Since you can't read your options, you made no good decision, so you are dead.")

