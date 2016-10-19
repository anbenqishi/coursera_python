# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

secret_number = 0
num_range = 100
count = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global count

    secret_number = random.randrange(0, num_range)
    count = int(math.ceil(math.log(num_range - 0 + 1, 2)))


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range

    print "New game. Range is from 0 to 100"
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range

    print "New game. Range is from 0 to 1000"
    num_range = 1000
    new_game()

def input_guess(guess):
    # main game logic goes here
    global count

    number = int(guess)
    print "Guess was ", number

    if count == 0:
        print "There's no more guess left."
        frame.stop()

    count = count - 1
    print "Number of remaining guesses is ", count

    right_answer = False
    if secret_number > number:
        print "Higher\n"
    elif secret_number < number:
        print "Lower\n"
    else:
        print "Correct\n"
        right_answer = True
        new_game()
    if count == 0 and not right_answer:
        print "Out of luck this time.\n"
        frame.stop()

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Number", input_guess, 50)

# call new_game
new_game()
frame.start()
# always remember to check your completed program against the grading rubric
