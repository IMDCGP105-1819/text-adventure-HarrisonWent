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
        room_doors = get_doors(f)
        f.close()

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
                if len(room_items) == 0:
                    print("You didn't find anything!")

            #Check inventory
            if user_input == "checkinventory":
                used_command = True
                if len(my_inventory_of_keys) == 0:
                    print("There are no items in your inventory!")
                else:
                    print("ITEMS IN YOUR INVENTORY:")
                    for keys in my_inventory_of_keys:
                        print(keys["KeyName"])

            #Interact with items
            for items in room_items:
                if items["ItemName"] in user_input:
                    for phrases in items["InteractPhrases"]:
                        if phrases in user_input:
                            used_command = True
                            if not searched_Room:
                                print("You haven't searched the room yet!")
                            else:
                                print(items["ItemDescription"])
                                if items["IsKeyFor"] != "null":
                                    print("you pick it up and put it in your backpack")
                                    my_inventory_of_keys.append({"KeyName": items["ItemName"]})
                                if items["EndsGame"] == "true":
                                    moving_out_of_room = True
                                    game_complete = True

            #Help options
            if(user_input.__contains__("help")):
                used_command = True
                print("AVAILABLE COMMANDS:")
                print(": Check inventory")
                if not searched_Room:
                    print(": Search room")
                else:
                    print("ITEMS IN ROOM:")
                    for items in room_items:
                        print(": ",items["InteractPhrases"]," :",items["ItemName"])
                print("DOORS IN ROOM:")
                for doors in room_doors:
                    if doors["Name"] != "null":
                        print("Open:", doors)


            #Open doors
            if "open" in user_input or "go" in user_input:
                for doors in room_doors:
                    if doors["Name"] in user_input or doors["Direction"] in user_input:
                        used_command = True
                        if doors["Name"] != "null":
                            Has_Key = get_room_key_requirement(doors["Name"],my_inventory_of_keys)
                            if Has_Key:
                                print("open door to the", doors["Direction"])
                                current_room = doors["Name"]
                                moving_out_of_room = True
                            else:
                                print("Look like that require some sort of key!")
                        else:
                            print("There is no door there")

            #command not understood
            if not used_command:
                print("I don't understand that command (enter help for help)")

            clear()

        #prepare for next room
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


def filter_string(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace('\n', '').replace('\r', '')
    input_string = input_string.replace(' ', "")
    return input_string

def clean_string(input_string):
    input_string = filter_string(input_string)

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    temp = ""

    for char in input_string:
        if char not in punctuations:
            temp = temp + char
        input_string = temp
    return input_string

def create_list(input_string):
    input_string = filter_string(input_string)
    stripped_input = input_string
    return stripped_input.split(",")

def get_items(f, item_count):
    a=0
    items = []
    while a < item_count:
        items.append({"ItemName" : clean_string(f.readline()),
                      "ItemDescription" : f.readline(),
                      "IsKeyFor" : clean_string(f.readline()),
                      "InteractPhrases" : create_list(f.readline()),
                      "EndsGame" : clean_string(f.readline())})
        a+=1
    return items

def get_doors(f):
    rooms = []
    rooms.append({"Name" : clean_string(f.readline()), "Direction" : "north"})
    rooms.append({"Name": clean_string(f.readline()), "Direction": "east"})
    rooms.append({"Name": clean_string(f.readline()), "Direction": "south"})
    rooms.append({"Name": clean_string(f.readline()), "Direction": "west"})
    return rooms

def get_room_key_requirement(room_name, my_inventory):
    with open_room(room_name) as f:
        lines = f.read().splitlines()
        requires_key = clean_string(lines[-2])
        if requires_key == "false":
            return True
        else:
            key_name = clean_string(lines[-1])
            for keys in my_inventory:
                if keys["KeyName"] in key_name:
                    return True
        return False

run_adventure()