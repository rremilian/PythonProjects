import random

class Dice:

    def __init__(self):
        
        self.history = []
        self.get_sides()
        self.roll()
    
    def get_sides(self):
        sides = int(input("How many sides does your dice have? "))

        if sides > 0:
            self.sides = sides
            print(f"Your dice have {self.sides} sides.")
        else:
            print("Error! The dice must have an integer and positive number of sides")
            self.get_sides()
    
    def roll(self):

        value = random.randint(1,self.sides)
        print(f"You rolled a {value}")
        self.history.append(value)
        self.play_again()
        
    def play_again(self):
        choice = input("Do you want to roll again ? (press enter for yes, type n/N for no or type h/H for history) ")
        if choice == "" or choice.lower() == "y":
            self.roll()
        elif choice.lower() == "n":
            print("Thank you for playing")
        elif choice.lower() == "h":
            print(list(self.history))
            self.play_again()
        else:
            print("Please enter a valid value !")
            self.play_again()

          
d = Dice()
