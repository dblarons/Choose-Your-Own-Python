from sys import exit

def chapter_three():
    print "\nCHAPTER THREE: FRENEMIES\n"
    print "You ask the group what is going on."
    print "Shocked, they ask you if you remember anything."
    name = raw_input("They say that your name is ")
    print "The ship you are on is called the ENDEAVOR and you were recently raided by the menaces of the galaxy..."
    print "The DURG Dominion (Cue intense sound effects here)"
    print "Duh Duh Dummmm"
    print "1. What is the Durg Dominion?"
    print "2. Let's find other survivors and take this ship to safety!"

    the_durgs = raw_input("> ")

    # if the_durgs == "1":
        # NEXT ROOM HERE

   # elif the_durgs == "2":
        # FIND SURVIVORS ROOM HERE

   # else:
       # "I don't speak %r" % the_durgs
      #  chapter_three()
    

def chapter_three_alt():
    print "\nCHAPTER THREE: ALONE AGAIN\n"
    print "You shoot all three soldiers--one woman and two men-- and search their bodies."
    print "To your dismay, you find nothing but a few rations and a rifle."
    print "1. Take rifle"
    print "2. Leave rifle"

    rifle = raw_input("> ")

    #if rifle == "1":
       # print "You pick up the rifle and strap it around your shoulder."
       # rifle = True
        # NEED THE NEXT ROOM HERE

   # else:
      #  print "You leave the rifle and leave through the next door."
        # NEED THE NEXT ROOM HERE
        

def door_three():
    print "You enter the third door to find three wounded soldiers."
    print "You draw your blaster."
    print "1. Shoot them all"
    print "2. Ask them what is going on."

    three_hostages = raw_input("> ")

    if three_hostages == "1":
        chapter_three_alt()

    elif three_hostages == "2":
        chapter_three()

    else:
        print "Seriously? All you had to choose between was 1 and 2, but there you go again, choosing %r" % three_hostages
        three_hostages()
        
def door_two():
    print "You enter the second door, but find nothing but a few canteens and a broken galactic rifle."
    print "You leave the room."
    door_two = True
    chapter_two()
     

def door_one():
    print "You enter the first door hoping, or not hoping, to find the source of the mysterious scream."
    print "To your right you see a dead soldier."
    print "1. Scream like a little girl"
    print "2. Approach the dead man"

    dead_soldier = raw_input("> ")

    if dead_soldier == "1" or "2":
        door_one = True
        print "You are scared but you approach the man and hope for the best."
        print "As you draw near him, he suddenly opens his eyes."
        print "1. Shoot him"
        print "2. Talk to him"

        shoot_soldier = raw_input("> ")

        if shoot_soldier == "1":
            print "You shoot the man and leave the room."
            chapter_two()

        elif shoot_soldier == "2":
            print "You approach the man, hoping to ask about the ship and your past."
            dead("Suddenly, the soldier draws his gun and kills you!")

        else:
            print "I don't know what that means."
            dead("You are dead because you hesitated. The soldier killed you.")
    

def chapter_two():
    print "CHAPTER TWO: CURIOSITY KILLED THE CAT"
    print "You search the abandoned bridge for a few minutes."
    print "You find a few dead soldiers and some ripped up papers, but you do not remember what happened here."
    print "You stand in front of 3 closed doors."
    print "1. Door 1"
    print "2. Door 2"
    print "3. Door 3"

    three_doors = raw_input("> ")

    if three_doors == "1":
        door_one()

    elif three_doors == "2":
        door_two()

    elif three_doors == "3":
        door_three()

    else:
        print "%r is not a number between 1 and 3." % three_doors
        chapter_two()
        

def long_hallway():
    print "You walk down the long hallway and through the broken door into the main deck of the ship."
    print "Suddenly you hear a scream."
    print "1. Investigate the scream"
    print "2. Barricade yourself in a corner and hide"

    the_scream = raw_input("> ")

    if the_scream == "1":
        chapter_two()

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

print "\nThank you for playing The Durg Dominion!\n"

start()
