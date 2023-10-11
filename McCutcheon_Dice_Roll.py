# This program will Roll Dice

import random


# Set limits for the min and max the dice can land on

MIN = 1

MAX = 6

# Create the main function that we be called towards the end

def main():
    roll = 'y'


    # Need to create a while loop for the user input

    while roll == 'y' or roll == 'Y':
        print('Rolling the dice...')
        print('The values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Ask the user if they want to roll again

        roll = input('Would you like to roll the dice again? (y = yes): ')

# Call the main function

main()

              
