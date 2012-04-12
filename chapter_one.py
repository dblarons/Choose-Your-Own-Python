import chapter_two
from sys import exit

def long_hallway():
    print "You walk down the long hallway and through the broken door into the main deck of the ship."
    print "Suddenly you hear a scream."
    print "1. Investigate the scream"
    print "2. Barricade yourself in a corner and hide"

    the_scream = raw_input("> ")

    if the_scream == "1":
        chapter_two.chapter_two()

    elif the_scream == "2":
        print lightsaber
        print "You barricade yourself in a corner of the bridge like the coward that you are."
        print "After an hour of waiting, you must make a decision"
        print "1. Continue hiding"
        print "2. Investigate the ship"

        barricade = raw_input("> ")

        if barricade == "1":
            dead("The designer eliminates you for being a weeny.")

        elif barricade == "2":
            chapter_two()

        else:
            print "What is %r supposed to mean??" % barricade
            long_hallway()

    else:
        print "Do you eat %r? Yeah, I thought so. So don't type it." % the_scream
        long_hallway()

            
def stay_and_look():
    print "You stay in the room and find a chest with the same emblem on it as your pack."
    print "1. Open the chest"
    print "2. Leave the room"

    chest_room = raw_input("> ")

    if chest_room == "1":
        print "You open the chest and find a lightsaber."
        print "Astounded at this discovery, you clearly take the lightsaber."
        print "Don't you...?"

        lightsaber = raw_input("> ")

        if lightsaber == "yes":
            lightsaber = "and lightsaber"
            print "You take the lightsaber and leave the room."
            open_door()

        else:
            lightsaber = ""
            print "You leave the lightsaber and exit the room."
            open_door()

    else:
        print "You leave the room."
        open_door()


def open_door():
    print "You exit the room and find yourself in a long hallway with a broken door on the other side."
    print "1. Walk through the door."

    hallway_door = raw_input("> ")

    if hallway_door == "1":
        long_hallway()

    else:
        print "This is not the time for %r " % hallway_door
        print "Please choose a number."
        open_door()


def chapter_one():
    print "You take the items and get dressed."
    print "There is a closed door in front of you."
    print "1. Open door"
    print "2. Stay in the room and take a look around"
    
    first_room = raw_input("> ")

    if first_room == "1":
        open_door()

    elif first_room == "2":
        stay_and_look()

    else:
        print "I don't know what that means. Please choose a number."
        chapter_one()


def leave_items():
    print "You are going to need these items."
    print "1. Take the items."
    items = raw_input("> ")

    if items == "1":
        blaster = True
        chapter_one()

    else:
        print "I don't know what that means. Please choose a number."
        leave_items()


def start():
    print "CHAPTER ONE: THE FORGOTTEN VESSEL"
    print "You wake up on an abandoned space ship."
    print "There is a pair of clothes, a blaster, and a pack with a strange emblem on it."
    print "1. Take the items"
    print "2. Leave the items"

    items = raw_input("> ")

    if items == "2":
        leave_items()

    elif items == "1":
        blaster = True
        chapter_one()

    else:
        print "I don't know what that means. Please choose a number."
        start()


def dead(why):
    print why, "Good job!"
    print "Would you like to play again?"

    replay = raw_input("> ")

    if replay == "yes":
        start()

    else:
        exit()

print "\nThank you for playing Space Adventure!\n"

start()
