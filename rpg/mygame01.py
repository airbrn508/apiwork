#!/usr/bin/env python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
        RPG Game
        ========
        Commands:
          go [direction]
          get [item]
    ''')
    return


# Print a player's current status
def showStatus():
    print('-------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("------------------------------")
    return


#an inventory, which is initially empty
inventory = []

#a dictionary linking room to other rooms
rooms = {
    'Hall': {
        'east': 'Dining Room',
        'south': 'Kitchen',
        'item': 'key'
        },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
        },
    'Dining Room': {
        'north': 'Dining Room',
        'south': 'Garden',
        'west': 'Hall',
        'item': 'cookie'
        }
    }

# Start the player in the Hall
currentRoom = 'Hall'

showInstructions()

while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into a list array
    #eg typing 'go east' would give the list:
    #['go', 'east']
    move = ''
    while move == '':
        move = input('> ')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You cannot go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if 'item' is rooms[currentRoom] and move[1] in rooms[currentRomm]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('You just picked up', move[1])
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can not get', move[1])

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
        print('You throw a cookie at the Monster!')
        del rooms[currentRoom]['item']
        inventory.remove['cookie']

    ## If a player neters a rooms with the monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monter has got you... GAME OVER!')
        break

    if currentRoom == 'Garden' and 'key' in inventory:
        print('You use the key to open the door in the garden and escape the creepy monster')
        print('You win!')
        break


print('Thanks for playing!')

