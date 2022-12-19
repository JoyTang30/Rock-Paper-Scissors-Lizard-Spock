from ai import AI
from person import Person
import time

class Game:
    def __init__(self):
        self.players= ' '

    def start_game(self):
        print("Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK Game")
        print(" ")
        print( "each match will be best of three")
        time.sleep(3)
        self.players= input("How many are playing? input 1 or 2:")

        while self.players != "1" and self.players != "2":
            self.players= input("How many are playing? input 1 or 2:")

        print (" ")
        print("The rules of the game are:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        time.sleep(3)





    def play_game(self):
        pass

    def display_winner(self):
        pass

    def run_game(self):
        pass


class Single_Player(Game):
        def __init__(self) -> None:
            super().__init__()

        def play_game(self):
            win_1=0
            win_2=0

            player_1=Person()
            player_2=AI()
            while player_1.display_choice >2 and player_2.display_choice >2:
                player_1.display_choice=


class Multiplayer(Game):
        def __init__(self) -> None:
            super().__init__()
        def play_game(self):
            win_1=0
            win_2=0

            player_1=Person()
            Player_2=Person()

