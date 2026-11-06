from case import Case
from color import Color


class Board:

    def __init__(self):
        self.size = 8
        self.cases = []

        for row in range(self.size):
            ligne = []
            for column in range(self.size):
                ligne.append(Case(row, column))#

            self.cases.append(ligne)

    def get_case(self, row, column):
        return self.cases[row][column]
    
    def display(self):
        for i,row in enumerate(self.cases):
            print(" "+"+--" * self.size + "+")
            ligne = str(i+1)+""
            for case in row:
                if case.is_empty():
                    ligne += "|  "
                else:
                    ligne += "|" + case.get_contenu().name[0].upper()

            print(ligne + "|")
        print(" "+"+--" * self.size + "+")
        print("  " + "  ".join(str(i + 1) for i in range(self.size)))
    def case_candidates(self, color):

        directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

        candidates=[]


        pass
    def move_jouable(self, row, column, color):
        if row < 0 or row >= self.size or column < 0 or column >= self.size:
            return False
        
    def cases_jouables():
        pass
    def appliquer_flips():
        pass

