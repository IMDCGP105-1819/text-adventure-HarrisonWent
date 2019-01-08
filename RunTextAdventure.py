import os
def clear():
    os.system('cls')

def run_adventure():
    game_complete = False

    #Load default room
    f = open_room("Default")
    current_room = f.readline()
    f.close()

    while not game_complete:
        #open current room
        f = open_room(current_room)

        #read room description
        print(f.readline())

        item_count = int(f.readline())
        room_items = get_items(f,item_count)

        user_input = get_input()

        if user_input == "searchroom":
            for val in room_items:
                print("You can see " + val["ItemName"])
        #if(user_input == "interact with item"):
            #if( item wins game):
                #game_complete = True

        #if(pivkup item name):
            #add item to inventory
        #if(use item)
            #todo add lines for after interacting with item such as "you destroyed the reactor"

        #if(user input == help):
            #print commands avaliable

        #if(userinput == open #### door):
            #try to open door
            #if requires key
                #if have key
                    #say used key
                #else say require key
            #else
                #open room
        f.close()
        clear()

    exit()
    #TODO default text such as "You have" + item name

    #TODO storing picked up items

def open_room(name):
    name = name.rstrip()
    f = open("Rooms/"+name, "r")
    return f

def get_input():
    user_input = input("What shall i do?")
    return user_input

def get_items(f, item_count):
    a=0
    items = []
    while a < item_count:
        itemName = f.readline()
        itemDescription = f.readline()
        isKeyFor = f.readline()
        phrases = f.readline()
        gameEnder = f.readline()
        items.append({"ItemName" : itemName, "ItemDescription" : itemDescription,"IsKeyFor" : isKeyFor,"InteractPhrases" : phrases,"EndsGame" :gameEnder})
        a+=1
    return items


run_adventure()