from case import Case


class Board:

    def __init__(self):
        self.size = 8
        self.cases = []

        for row in range(self.size):
            ligne = []
            for column in range(self.size):
                ligne.append(Case(row, column))

            self.cases.append(ligne)
            print(self.cases)
    def get_case(self, row, column):
        return self.cases[row][column]
    def display(self):
        for row in self.cases:
            print("+--" * self.size + "+")
            ligne = ""
            for case in row:
                if case.is_empty():
                    ligne += "|  "
                else:
                    ligne += "| " + case.get_contenu().color[0].upper() + " "

            print(ligne + "|")
        print("+--" * self.size + "+")
    def move_jouable():
        pass    
    def cases_jouables():
        pass
    def appliquer_flips():
        pass