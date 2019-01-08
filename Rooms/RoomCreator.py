import os


def clear():
    os.system('cls')

def menu():
    choice = input("Set up rooms or set up defaults? Rooms/Defaults")

    clear()
    if choice == "Rooms":
        create_room()
    elif choice == "Defaults":
        create_defaults()
    else:
        menu()


def create_defaults():
    f = open("Default", "w+")
    start_room = input("Enter the name for the starting room:")
    f.write(start_room+"\n")
    end_script = input("Enter the dialogue for finishing the game")
    f.write(end_script)
    f.close()
    clear()
    menu()


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
    menu()


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
    item_count = int(input("Please enter how many items this room has, 0 for no items: "))
    f.write(str(item_count)+"\n")

    finished_items = 0

    while finished_items != item_count:
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

        item_interact_list = input("Please enter phrases that interact with this item e.g.(Pick up,Take : ")
        f.write(item_interact_list+"\n")

        item_end_game = input("Does this item end the game? True/False")
        f.write(item_end_game+"\n")

        finished_items += 1


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


menu()

