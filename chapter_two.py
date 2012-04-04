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
