import os

def clear():
    os.system('cls')

def run_adventure():

    game_complete = False

    #Load default room
    f = open_room("Default")
    current_room = f.readline()
    f.close()

    my_inventory_of_keys = []

    while not game_complete:

        #open current room
        f = open_room(current_room)
        searched_Room = False

        #read room description
        print(f.readline())

        #get room items
        item_count = int(f.readline())
        room_items = get_items(f,item_count)

        #actions while in room
        moving_out_of_room = False
        while not moving_out_of_room:
            user_input = get_input()
            used_command = False

            #Search room
            if user_input == "searchroom":
                used_command = True
                searched_Room = True
                for val in room_items:
                    print("You can see " + val["ItemName"])

            #Check inventory
            if user_input == "checkinventory":
                used_command = True
                if len(my_inventory_of_keys) == 0:
                    print("There are no items in your inventory!")
                else:
                    print("ITEMS IN YOUR INVENTORY:")
                    for a in my_inventory_of_keys:
                        print(a["KeyName"])

            #Interact with items
            # todo get item name and search if contains that pickup word
            for a in room_items:
                if user_input in clean_string(a["InteractPhrases"]):
                    used_command = True
                    if not searched_Room:
                        print("You haven't searched the room yet!")
                    else:
                        print(a["ItemDescription"])
                        if a["IsKeyFor"] != "null":
                            print("you pick it up and put it in your backpack")
                            my_inventory_of_keys.append({"KeyName": a["ItemName"]})
                        if a["EndsGame"] == "true":
                            game_complete = True

            #if(use item)
                #todo add lines for after interacting with item such as "you destroyed the reactor"

            #Help options
            if(user_input.__contains__("help")):
                used_command = True
                print("AVALIABLE COMMANDS:")
                print(": Check inventory")
                if not searched_Room:
                    print(": Search room")
                else:
                    for a in room_items:
                        print(": ",a["InteractPhrases"]," :",a["ItemName"])

            #command not understood
            if not used_command:
                print("I don't understand that command")

            #todo open doors
            #if(userinput == open #### door):
                #try to open door
                #if requires key
                    #if have key
                        #say used key
                    #else say require key
                #else
                    #open room

            input()
            clear()
        #prepare for next room
        f.close()
        clear()

    #Finish game
    f = open_room("Default")
    f.readline()
    print(f.readline())
    input()
    f.close()

    exit()

def open_room(name):
    name = name.rstrip()
    f = open("Rooms/"+name, "r")
    return f

def get_input():
    user_input = input("What shall i do? (enter HELP for help)")
    user_input = clean_string(user_input)
    return user_input

def clean_string(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace(' ', "")

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    temp = ""
    for char in input_string:
        if char not in punctuations:
            temp = temp + char
        input_string = temp
    return input_string

def get_items(f, item_count):
    a=0
    items = []
    while a < item_count:
        items.append({"ItemName" : f.readline().replace('\n', '').replace('\r', ''),
                      "ItemDescription" : f.readline().replace('\n', '').replace('\r', ''),
                      "IsKeyFor" : f.readline().replace('\n', '').replace('\r', ''),
                      "InteractPhrases" : f.readline().replace('\n', '').replace('\r', ''),
                      "EndsGame" : f.readline().replace('\n', '').replace('\r', '')})
        a+=1
    return items


run_adventure()