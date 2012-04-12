from sys import exit
from random import randint

# sets up a class Game()
class Game(object):

    # a special initialization method that sets up
    # important variables.
    def __init__(self, start):

        # initializes the self.lols variable
        self.lols = [
            "You lost? My dog can even beat this game.",
            "Were you even trying?",
            "Nice try. Wait no, nevermind."
        ]
        # initializes the self.start variable and assigns
        # it to start
        self.start = start

    # I believe that this is sort of the mechanism that drives
    # the entire game.
    def play(self):
        next = self.start

        while True:
            print "\n--------------------------"
            room = getattr(self, next) # sets room equal to self.next
            next = room()

    def death(self):
        print self.lols[randint(0, len(self.lols)-1)]

        replay = raw_input("[play again?]> ")

        if replay == 'yes':
            a_game = Game("chapter_one")
            a_game.play()

	elif replay == 'no':
	    exit(1)

        else:
            print "I don't know what %s means." % replay
	    return 'death'

    def chapter_one(self):
        print "You are riding your horse alongside a speeding train."
        print 'You and your gang, "The yellow monkeys", are about'
        print "to hold up the passengertrain and take all the valuables that"
        print "you can get your grubby hands on."
        print "\n"
        print "As you pass by the first passenger car a security"
        print "officer pulls out his colt pistol and takes aim...."
        print "AT YOU!!!!"
        
        action = raw_input("> ")

        if action == "jump on the train":
            print "You try to balance on the horse and prepare to"
            print "jump onto the train. With steady balance you stand"
            print "up and prepare to jump."
            print "\n"
            print "The guard fires off two missing shots, but his third"
            print "hits its mark. The bullet knocks you off your horse"
            print "and you die when your soft skull hits the hard ground."
            return 'death'

        elif action == "shoot":
            print "Like a seasoned criminal, you quickly draw your"
            print "weapon and take aim at the guard."
            print "The poor bloke is dead before he can shoot at you."
            return 'second_car'
        
        else:
            print "I don't know what that means."
            return 'chapter_one'

    def second_car(self):
        print "Your trusty stallion, Happy, speeds up and approaches"
        print "the second passenger car."
        print "\n"
        print "This car is not protected by a guard, so you can"
        print "board the train in safety."

        action = raw_input("> ")

        if action == "keep riding":
            print "You keep on riding alongside the train."
            print "Your horse begins to tire, as it cannot keep"
            print "up with the fast train for forever."
            print "\n"
            print "Happy slows down and loses the train."
            print "You lose."
            return 'death'

        elif action == "board the train":
            print "You put your gun in its holster and try to balance"
            print "on Happy. You stand up and balance for a moment"
            print "before you leap onto the horse."
            print "\n"
            print "You made it!"
            print "You land face down on the top of the second passenger"
            print "car. There is a hatch on the top of the car, but it"
            print "is protected by a rustic 1 digit code."
            print "If you get the code wrong 8 times, you will be locked"
            print "out for good."

            code = "%d" % (randint(0,9))
            guess = raw_input("[keypad]> ")
            guesses = 0

            while guess != code and guesses < 8:
                print "BZZZZZZEDDD!"
                guesses += 1
                guess = raw_input("[keypad]> ")

            if guess == code:
                print "The hatch clicks open!"
                print "You climb into the second passenger car."
                return 'inside_train'

            else:
                print "The lock buzzes the last time and you are locked"
                print "out and stuck on the top of the train."
                print "You lose."
                return 'death'

	else:
		print "How am I supposed to know what %s means?" % action
		return 'second_car'


    def inside_train(self):
	print "You look around to see frightened passengers shaking in"
	print "their seats. You pull out your colt revolver and fire a few"
	print "shots into the ceiling to show that your the real deal."
	print "\n"
	print 'You yell over the chugging train engines, "Everyone,'
	print 'put your valuables in the center isles. If I find out that'
	print 'ANYONE is hiding theirs from me, I will shoot them myself."'
	print 'One passenger jumps out of his seat and hurls himself toward you.'
	
	action = raw_input("> ")

	if action == "dodge" or "duck":
	    print "You attempt to dodge the large man who hurtles"
	    print "toward you. You dive into the passenger seat beside"
	    print "you and cover your head. Suddenly, the woman in"
	    print "the seat that you just jumped into grabs your colt"
	    print "and aims it at your head."
	    print "You lose."
	    return 'death'

	elif action == "shoot" or "kill him":
	    print "You quickly grab your colt and shoot the man who"
	    print "hurdles toward you. His body crashes down on you"
	    print "and knocks your colt onto the floor. Struggling to"
	    print "stand up, you see a brave woman reach for the"
	    print "revolver and aim it at you."
	    print "You lose."

	elif action == "take hostage":
	    print "Reacting quickly, you grab the pretty young lady"
	    print "who sits in the seat next to where you are standing."
	    print "You hold her in front of her with the gun to her neck."
	    print "The man who is hurtling toward you sees this and"
	    print "turns to miss you and the young lady."
	    print "Deciding that you might be safer with a hostage,"
	    print "you decide to bring her along."
	    return 'third car'

	else:
	    print "Sorry, doing %s is not an option." % action
            
        

a_game = Game("chapter_one") # insert the start of the game here.
a_game.play()
