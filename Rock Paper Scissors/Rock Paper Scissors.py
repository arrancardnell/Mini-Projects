from random import randint

player_score = 0
computer_score = 0

play_again = True

print("\tWelcome to Rock, Paper, Scissors!")
print("\nRock beats Scissors. Scissors beat Paper. Paper beats Rock.")
print("\nMake a better choice than your opponent to win. Good luck!")

while play_again != False:
    
    print("\nWhat would you like to pick?")
    player_choice = input("> ").lower()

    if player_choice == "rock":
        print("\nYou chose rock.")
        player_choice = 1
    elif player_choice == "paper":
        ("\nYou chose paper.")
        player_choice = 2
    elif player_choice == "scissors":
        ("\nYou chose scissors.")
        player_choice = 3
    else:
        print("Please pick Rock, Paper or Scissors")
        continue

    computer_choice = randint(1,3)

    if player_choice == 1:
        if computer_choice == 1:
            print("\nThe computer chooses rock.")
            print("\nIt's a draw!")
        elif computer_choice == 2:
            print("\nThe computer chooses paper.")
            print("\nThe computer wins. Better luck next time!")
            computer_score += 1
        else:
            print("\nThe computer chooses scissors.")
            print("\nYou win! Congratulations!")
            player_score += 1
    elif player_choice == 2:
        if computer_choice == 1:
            print("\nThe computer chooses rock.")
            print("\nYou win! Congratulations!")
            player_score += 1
        elif computer_choice == 2:
            print("\nThe computer chooses paper.")
            print("\nIt's a draw!")
        else:
            print("\nThe computer chooses scissors.")
            print("\nThe computer wins. Better luck next time!")
            computer_score += 1
    else:
        if computer_choice == 1:
            print("\nThe computer chooses rock.")
            print("\nThe computer wins. Better luck next time!")
            computer_score += 1
        elif computer_choice == 2:
            print("\nThe computer chooses paper.")
            print("\nYou win! Congratulations!")
            player_score += 1
        else:
            print("\nThe computer chooses scissors.")
            print("\nIt's a draw!")

    print("\nThe current scores are:\n Player: ", player_score, "\tComputer: ", computer_score)

    print("\nWould you like to play again?")
    answer = input("> ").lower()

    if answer not in ("yes", "y"):
        play_again = False
