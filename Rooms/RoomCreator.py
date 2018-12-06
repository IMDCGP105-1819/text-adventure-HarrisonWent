import os


def clear():
    os.system('cls')


def create_room():

    finished_rooms = False
    while not finished_rooms:
        f = set_up_room()

        print("ROOM ITEMS")

        set_up_items(f)

        print("ROOM DOORS")

        set_up_doors(f)

        print("ROOM KEY REQUIREMENTS")

        set_up_keys(f)

        f.close()

        finished_rooms = input("Create another room? True/False: ")
        clear()


def set_up_room():
    print("ROOM NAME")

    room_name = input("Please enter room name: ")

    name_found = False

    while not name_found:
        if verify_room_name(room_name):
            f = open(room_name, "w+")
            name_found = True
        else:
            overwrite = input("That name is already in use for another room. overwrite? True/False: ")
            if overwrite == "True":
                f = open(room_name, "w+")
                name_found = True

    room_description = input("Please enter a description for the room listing story and exits: ")
    f.write(room_description+"\n")
    return f


def verify_room_name(room_name):
    try:
        open(room_name, "r")
        return 0
    except IOError:
        return 1


def set_up_items(f):
    finished_items = False

    while finished_items != "False":
        new_item = input("Please enter an item for the room: ")
        new_item_description = input("Please enter a description for the new item: ")
        new_item_is_key = input("Is this item a key? True/False: ")

        if new_item_is_key:
            item_unlock_room = input("Please enter the room name this item unlocks: ")
        else:
            item_unlock_room = "null"

        f.write(new_item+"\n")
        f.write(new_item_description+"\n")
        f.write(item_unlock_room+"\n")

        finished_items = input("Enter another item to the room? True/False: ")


def set_up_doors(f):
    confirm = input("Does the room have a door to the NORTH? True/False: ")
    if confirm == "True":
        room_north = input("Please enter room NORTH name: ")
    else:
        room_north = "null"

    confirm = input("Does the room have a door to the EAST? True/False: ")
    if confirm == "True":
        room_east = input("Please enter room EAST name: ")
    else:
        room_east = "null"

    confirm = input("Does the room have a door to the SOUTH? True/False: ")
    if confirm == "True":
        room_south = input("Please enter room SOUTH name: ")
    else:
        room_south = "null"

    confirm = input("Does the room have a door to the WEST? True/False: ")
    if confirm == "True":
        room_west = input("Please enter room WEST name: ")
    else:
        room_west = "null"

    f.write(room_north+"\n")
    f.write(room_east+"\n")
    f.write(room_south+"\n")
    f.write(room_west+"\n")


def set_up_keys(f):
    requires_key = input("Does this room require a key to access? True/False: ")
    if requires_key == "True":
        key_requirement = input("Name the key to unlock this room: ")
    else:
        key_requirement = "null"

    f.write(requires_key+"\n")
    f.write(key_requirement+"\n")


create_room()

