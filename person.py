import time
class Person:

    def __init__(self):
        self.choice_list= ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']


    def display_choice(self):
        print(" ")
        print("Choose 0 for ROCK")
        print("Choose 1 for PAPER")
        print("Choose 2 for SCISSORS")
        print("Choose 3 for LIZARD")
        print("Choose 4 for SPOCK")

        self.person_choice= input("Choose your Gesture")

        print(self.choice_list[int(self.person_choice)])
        return self.choice_list[int(self.person_choice)]    