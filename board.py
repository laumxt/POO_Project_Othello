from case import Case


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
                    ligne += "|" + case.get_contenu().color[0].upper()

            print(ligne + "|")
        print(" "+"+--" * self.size + "+")
        print("  " + "  ".join(str(i + 1) for i in range(self.size)))
    
    def move_jouable():
        pass    
    def cases_jouables():
        pass
    def appliquer_flips():
        pass

