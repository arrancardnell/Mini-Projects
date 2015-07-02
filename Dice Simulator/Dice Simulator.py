# Dice simulator
# User selects the number of dice they wish to roll and the program will
# simulate a roll of the dice. The program will then display the values
# and calculate the total if necessay.

from random import *

def dice_roll(number):

    # dict values made up of all the segments needed to create any die value
    dice_images = {0:'   .-------.',
                   1:'   |       |',
                   2:'   |   0   |',
                   3:'   |     0 |',
                   4:'   | 0     |',
                   5:'   | 0   0 |',
                   6:"   '-------'"}

    # tuples for each value of the dice (1-6) using the dict values in dict_images
    dice_values = ((0, 1, 2, 1, 6),
                   (0, 4, 1, 3, 6),
                   (0, 4, 2, 3, 6),
                   (0, 5, 1, 5, 6),
                   (0, 5, 2, 5, 6),
                   (0, 5, 5, 5, 6))

    dice_side = []
    # create a list of all the images that make up the required side of the dice
    for value in dice_values[number-1]:
        dice_side.append(dice_images[value])
    # iterate through the list and print out the selected side
    for side in dice_side:
        print(side)

def roll():

    return randint(1, 6)

def number_of_dice():

    print("Welcome to Dice Roll Simulator!")
    print("How many dice would you like to roll? (Choose between 1-4)")

    dice_number = int(input("> "))

    while dice_number not in range(1,5):
        print("Please select a value between 1 and 4")
        dice_number = int(input("> "))

    print("You have selected", dice_number)
    print("The dice will now be rolled. Good luck!")

    dice_values = []
    for i in range(dice_number):
        roll_value = roll()
        dice_values.append(roll_value)
    
    for value in dice_values:
        dice_roll(value)


    total = 0
    for x in dice_values:
        total = total + x

    print("\nThe total is:", total)


roll_again = True

while roll_again:
    number_of_dice()

    print("Would you like to roll again?")
    answer = input("> ").lower()

    if answer not in ("yes", "y"):
        print("I hate you. Goodbye.")
        roll_again = False
    
