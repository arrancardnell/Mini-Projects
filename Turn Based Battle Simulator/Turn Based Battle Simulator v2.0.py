# Turn Based Battle Simulator v2.0

# Player and computer take it in turns to attack each other with different moves
# until one is defeated. This version was created to 'simplify' the code with
# classes.

import random

class Player(object):

    def __init__(self, name):
        self.name = name
        self.moves = {"Punch": [18, 25],
                      "Mega Punch": [10, 35],
                      "Heal": [-25, -20]
                      }
        self.moves_list = list(self.moves)
        self.moves_list_lower = [move.lower() for move in self.moves_list]
        self.move_names = '\n'+'\n'.join(
            "{0}. {1} (Deal damage between '{2[0]}' - '{2[1]}')".format(
                i,
                move,
                self.moves[move]
                )
            for i, move in enumerate(self.moves_list)
            )

    def select_move(self):
        move = input(self.move_names + '\n> ').lower()
        try:
            return self.moves_list[int(move)]
        except ValueError:
            return self.moves_list[self.move_list_lower.index(move)]
        except IndexError:
            print("That is not valid move. Please try again.")
            
    def use_move(self, move):

        if random.randint(1,5) == 1:
            print("{} missed!".format(self.name.capitalize()))
        else:
            magnitude = random.randint(*self.moves[move])
            return magnitude
            
class Computer(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        
    def select_move(self):
        pass

def main():
    """Main function that will welcome the player to the game."""

    opening = ['Welcome to Battle Sim! This is a turn based combat simulator where',
           'there can only be one winner.',
           '\nHow to play.\n\nPlayers take turn to choose a move. Moves can either deal moderate damage',
           'with a low range, deal high damage but over a wide range, or they can',
           'heal. (Note: Moves can miss, including Heal!)',
           '\nEach player starts with 100 health, and the first player to reduce their',
           'opponent to 0 is the winner.'
           ]

    for line in opening:
        print(line, sep='\n')

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 100

        player = Player("You")
        computer = Computer("Opponent")
    # determine whose turn it is
        turn = random.randint(0,1) # heads or tails
        if turn:
            player_turn = True
            computer_turn = False
            print("\nPlayer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nComputer will go first.")

        print("\nPlayer health: ", player_health, "Computer health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            if player_turn:
                player_damage = player.use_move(player.select_move())
                if player_damage < 0:
                    player_health -= player_damage
                    if player_health > 100:
                        player_health = 100 # cap max health at 100. No over healing!
                else:
                    computer_health -= player_damage
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Player"
                        break
            else:
                computer_move = computer.select_move()

            player_turn = not player_turn
            computer_turn = not computer_turn

        if winner == "Player":
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nCongratulations! You have won. You're an animal!!")
        else:
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. Better luck next time.")

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
