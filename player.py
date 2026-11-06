from board import Board
from session import Session


class Player:
    def __init__(self, color, session: Session, mon_tour=False):
        self.color = color
        self.session = session
        self.mon_tour = mon_tour

    def tour(self):
        if self.color == self.session.tour_joueur:
            if Board.move_jouable(self.color):
                self.mon_tour = True
            else:
                self.mon_tour = False