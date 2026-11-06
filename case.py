from pawn import Pawn
from pawn import Color
class Case:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.contenu = None

    def is_empty(self):
        return self.contenu is None

    def get_contenu(self):
        return self.contenu

    def place_pawn(self, pawn):
        if self.is_empty():
            self.contenu = pawn
            return True
        return False

    def remove_pawn(self):
        self.contenu = None