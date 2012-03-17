print "Welcome!"
print "Please type in lower case characters."

raw_input("To play, please press enter: ")

print "\nYou wake up in the middle of a green field with the bright morning sun shining on your face."
print "Beside you lie a rustic sword, an empty bottle, and a pair of clothes with a small traveling bag."
print "Pick up the items?\n"

items = raw_input("> ")

if items == "yes":
    print "\nYou put on the clothes, strap the sword around your belt, and place the bottle \nin your traveling bag."
    print "Still in a haze and suffering from memory loss, you take a brief look around."
    print "To your LEFT is a small brook, and to your RIGHT is a mysteriously cloaked figure."
    print "In which direction do you wish to travel?\n"

    brook_man = raw_input("> ")

    if brook_man == "left":
        print "\nYou arrive at the small brook."
        print "Do you wish to FILL your bottle or FOLLOW the stream north?\n"

        brook_fill_follow = raw_input("> ")

        if brook_fill_follow == "fill":
            print "\nYou crouch down and fill your bottle."
            print "You are suddenly stabbed in the back.\n"
            print "THE END. \n" # END OF GAME

        elif brook_fill_follow == "follow":
            print "\nYou follow the stream north and try to remember your past."
            print "As you walk, you notice that the hooded figure you saw earlier is following you. \n"
            print "1. Keep walking NORTH and ignore him."
            print "2. Draw your sword and prepare for BATTLE."
            print "3. Stop at the creek, fill your bottle, and offer the man a DRINK. \n"

            follow = raw_input("> ")

            if follow == "north":
                print "\nIgnoring the man, you continue walking North."
                print "Just as you remember your name, you are stabbed in the back and die."
                print "THE END. \n" # END OF GAME

            elif follow == "battle" or follow == "drink":
                print "\nYou turn and approach the hooded figure."
                print "As you near him, he removes his hood and you are knocked back by a sudden flood of memories. \n"
                name = raw_input("You remember that your name is ")
                print "\n\"%s,\" the man shouts." % name
                print "You remember that the man is your elder brother, and that you \nrecently went on an adventure with him."
                print "\"What happened to you?\" he asks.\n"
                print "1. I don't know! My memory is GONE."
                print "2. You're a liar! I know that you're the WIZARD.\n"

                gone_wizard = raw_input("> ")
                if gone_wizard == "gone":
                        print "\n\"Tell me everything you remember,\" your brother says."
                        print """After telling him all of your memories, you awake from a dream to find
that you have been tricked by a wily wizard into giving the location of your
beloved brother away. """
                        print "The wizard uses his magic to enslave you, but you valiantly resist and die. \n"
                            
                        print "THE END. \n" # END OF GAME
                        
                elif gone_wizard == "wizard":
                        print "\nSure enough, you awake from this false reality to find yourself in a dark dungeon."
                        print "You are able to escape your restraints, kill the wizard, and rescue your brother."
                        print "By the way, your brother was also captured by the wizard."
                        print "YOU WIN!!!\n"
                        raw_input("PRESS ENTER YOU WINNER!!")
                        raw_input("CONGRATULATIONS!!")
                        raw_input("STELLAR JOB!!")

                else:
                        print "\nYou don't respond because your larynx has just been punctured by a bee sting."
                        print "THE END. \n" # END OF GAME
    
        else:
            print "\nYour liver fails."
            print "THE END. \n" # END OF GAME

    elif brook_man == "right":
        print "\nYou draw near the hooded figure and grasp your archaic sword with your right hand."
        print "You recognize this man, although you do not know from where. \n"
        print "1: GREET the man as a fellow traveller."
        print "2: DRAW your sword and face the man in battle."
        print "3: RUN away.\n"

        man_interact = raw_input("> ")

        if man_interact == "greet" or man_interact == "draw" or man_interact == "run":
            print "\nYou are killed by the designer."
            print "THE END. \n" # END OF GAME
        else:
            print "\nYou die from unknown causes."
            print "THE END. \n" # END OF GAME

    else:
        print "You have a heart attack and die."
        print "THE END. \n" # END OF GAME

else:
    print "Weaponless, thirsty, and in only your undergarments, you die."
    print "THE END." # END OF GAME
    
print "Would you like to see the credits?"

the_end = raw_input("> ")

if the_end == "yes":
    print "\nDesign: Aaron "
    print "Testing: Isaac\n"
    print "Thank you for playing."

else:
    print "Thank you for playing."
