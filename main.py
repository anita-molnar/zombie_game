from room import Room
from character import Enemy, Character

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room, buzzing with flies.")

ballroom = Room("Ballroom")
ballroom.set_description("A fancy ballroom.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A fancy dining hall.")

# room links
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# set the enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi my name is Dave, I'd like to eat your brain.")
dave.set_weakness("cheese")

# set friend
morphy = Character("Morphy", "A friendly man")
morphy.set_conversation("""My name is Morphy, a hint how to kill the zombie: 
I am yellow or white, a diary delight,
Spread on crackers or on a toast,
The zombie least favourite food!
I know its cheesy..:).Go and fend yourself!!!""")

# Characters locations
kitchen.set_character(dave) 
ballroom.set_character(morphy)

# loop of the game 
current_room = dining_hall
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    # if there is someone in the room
    if inhabitant is not None:
        # if enemy
        if inhabitant.is_enemy():
            inhabitant.describe()
            print("What do you like to do? Type: 'talk' 'fight' ")
            user_answer = input("> ").lower()
            if user_answer == "talk":
                inhabitant.talk()
            elif user_answer == "fight":
                print("type his weakness")
                user_answer = input("> ").lower()
                inhabitant.fight(user_answer)  
        # if a character
        else:
            inhabitant.describe()
            print("what do you want to do? Type: 'talk', 'move' or 'hug'")
            user_answer = input("> ").lower()
            if user_answer == "talk":
                inhabitant.talk()
            elif user_answer == "move":
                pass
            elif user_answer == "hug":
                print("Thank you for your hug!")
    
    print("Which direction would you like to go? North, east, south, west")
    command = input("\n> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        pass
    