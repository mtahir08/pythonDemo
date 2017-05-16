###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
three_digits = digits[:3]
print(three_digits)

# Another hint:
guess = list(input("What is your guess? "))
guess = [int(x) for x in guess]
print(guess)

def check_guessing():
    if guess == three_digits:
        return "Wow!!! you guesses"
    elif guess[0] in three_digits and guess[1] in three_digits and guess[2] in three_digits:
        return "you guessed with wrong position"
    else:
        return "Sorry!! you did not guess correct!!"

if len(guess) != 3:
    print "Please enter 3 digits"
else:
    result = check_guessing();
    print(result)         
# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
