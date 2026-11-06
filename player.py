from board import Board 
from session import Session


class Player:
    def __init__(self, color, mon_tour=False):
        self.color = color
        self.mon_tour = mon_tour

    def tour(self):
        if self.mon_tour == Session.tour_joueur:
            if Board.move_jouable(self.color):
                self.mon_tour = True
            else:
                self.mon_tour = False

#test 
player=Player("black", True)
print(player.color)
Session.tour_joueur = True
Board.move_jouable = lambda color: True  # Mocking the method for testing
print(player.mon_tour)