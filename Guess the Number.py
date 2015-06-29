# Guess the Number

# Game where a random number is selected at the start and the user must try to
# guess the number correctly using the hints before the attempts run out.

import random

def main():
    welcome = ['Welcome to Guess the Number! This is a game where a number',
               'is selected at random which the player must guess correctly',
               'in a certain number of attempts. If the player guesses incorrectly',
               'the player will be given a hint to help them with their next guess.',
               ]

    for line in welcome:
        print(line, sep='\n')

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        number = random.randint(1,100)
        guess = None
        attempts = 10
        while (number != guess and attempts != 0):
            print(("\nYou have {} attempts remaining.").format(attempts))
            try:
                guess = int(input("\nPick a number between 1-100" + "\n>")) 
            except ValueError: # check the input is an integer
                print("That is not a number. Please try again.")
            else: # check the input is within the range
                if 1 <= guess < 100:
                    pass
                else:
                    print("Your number is out of range. Try again.")
                    continue

            comparison = number - guess

            # compare the guess to the actual number. If positive,
            # the guess was too low. If negative, too high.

            if comparison < 0:
                print("\nYour guess was too high. Try guessing lower next time.")
            elif comparison > 0:
                print("\nYour guess was too low. Try guessing higher next time.")

            attempts -= 1 # reduce the number of attempts by 1

        if number == guess:
            print("\nCongratulations! You guessed correctly. You rock!")
        else:
            print("\nBetter luck next time!")

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
