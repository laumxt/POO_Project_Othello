from board import Board
from session import Session


class Player:
    def __init__(self, color, mon_tour=False):
        self.color = color
        self.mon_tour = mon_tour

    