#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
      print('You see a '+ rooms[currentRoom]['item']+': '+ rooms[currentRoom]['description'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Attic',
                  'item'  : 'key',
                  'description' : 'DESCRIPTION: A key can be used to open a locked object.',
                },
            'Attic' : { #added attic room
                  'east' : 'Hall',
                  'item' : 'sword',
                  'description':'DESCRIPTION: A sword can be used during battle.'

                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east'  : 'Garden',
                  'item'  : 'monster',
                  'description': 'DESCRIPTION: This monster is blue colored and loves cookies.',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Trap Room',
                  'north' : 'Pantry',
                  'item' : 'potion',
                  'description' : 'DESCRIPTION: Potion can be used anytime to increase your stamina.',
               },
            'Trap Room' : {#added trap room
                },
            'Garden' : {
                  'north' : 'Dining Room',
                  'west' : 'Kitchen',
                  'east' : 'Trap Room',
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
                  'description':'DESCRIPTION: Yummmmm!!!! Cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('That path leads to nowhere.')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  #added a functionality to use an item
  #if they type 'use'
  if move[0] == 'use':
    if move[1] in inventory:
      #remove item from inventory once it is used
      inventory.remove(move[1])
      #display a message
      print (move[1] + ' used')
      
    #otherwise if no item is present in inventory display a message
    else:
      print(f"Can't use {move[1]}, since you do not have that item to use")

  ## Define how a player can win
  ##if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
  ##  print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
  ##  break

  #New conditions set for the player to win
  if currentRoom == 'Kitchen' and 'cookie' in inventory and 'sword' in inventory:
      print('Oh no. You are now in the Kitchen, and there is a monster here\n ')
      choice=input('What do you want to do: 1. use cookie 2. use sword 3. run \n>')
      if choice.lower()=='use cookie' or choice=='1':
        print('You gave cookie to the monster. Monster is busy eating the cookie. You attack the monster with the sword and kill it..... YOU WIN!!!!!')
        break
      elif choice.lower()=='use sword' or choice=='2':
        print('You attacked the monster with a sword. Monster overpowered you and tore you in half. You are dead!!')
        break
      else:
        print('The monster got to you. You died')
        break
  
  ## If a player enters a room with a monster
  elif currentRoom == 'Kitchen':
    print('A moster got to you and tore you in half...... GAME OVER!!')
    break
  ##elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
  ##  print('A monster has got you... GAME OVER!')
  ##  break
  
  if currentRoom == 'Attic' and 'sword' in inventory:
      #added slide function to lure user to get to trap room faster
      slide=input('Wohoo!! Getting the sword unlocked a slide. Do you want to go down the slide (Y or N) \n>')
      if slide.lower() == 'y':
         print ("It was fun while you were sliding down. However this slide led you straight to the trap room. You meet your end. \n Your remains were found later by another unlucky adventurer.")
         break
      #elif slide.lower() == 'n':
      #   currentRoom=='Attic'
      else:
         currentRoom == 'Attic'
  if currentRoom == 'Trap Room':
    print('You walked right into the trap room. There is no getting out. You starved to death!!!! GAME OVER!!!!')
    break
      
         
