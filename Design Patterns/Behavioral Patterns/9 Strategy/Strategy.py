import random
from abc import ABC, abstractmethod

class Strategy(ABC):
    def selection(self):
        pass
    
class Fish(Strategy):
  
    def selection(self):
        return "Fish"

class Bbq(Strategy):
    def selection(self):
        return "Bbq"

class Water(Strategy):
    def selection(self):
        return "Water"

class Random(Strategy):
    def selection(self):
        options = ["Fish", "Bbq", "Water"]
        return random.choice(options)

class Game:
    strategy: Strategy

    def __init__(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec):
        s1 = self.strategy.selection()
        s2 = sec.strategy.selection()
        if s1 == s2:
            print("It's a tie")
        elif s1 == "Fish":
            if s2 == "Water":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Bbq":
            if s2 == "Fish":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Water":
            if s2 == "Bbq":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

player1 = Game(Water())

player2 = Game(Fish())

player1.play(player2)