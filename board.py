from case import Case
from color import Color


class Board:
    DIRECTIONS = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

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
            ligne = str(i)+""
            for case in row:
                if case.is_empty():
                    ligne += "|  "
                else:
                    ligne += "| " + case.get_contenu().color.name[0].upper()

            print(ligne + "|")
        print(" "+"+--" * self.size + "+")
        print("  " + "  ".join(str(i) for i in range(self.size)))



    def case_candidates(self, color):

        candidates=[]
        

        for row in range(self.size):
            for column in range(self.size):
                case = self.get_case(row, column)
                
                if not case.is_empty() and case.get_contenu().color != color:

                    for dr, dc in self.DIRECTIONS:
                        r = row + dr
                        c = column + dc

                        if 0 <= r < self.size and 0 <= c < self.size:
                            voisin = self.get_case(r,c)

                            if voisin.is_empty() and (r,c) not in candidates:
                                candidates.append((r,c))
        return candidates


    
    def move_jouable(self, row, column, color):
        if row < 0 or row >= self.size or column < 0 or column >= self.size:
            return False
        if not self.get_case(row,column).is_empty():
            return False
        directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

        for dr, dc in directions:
            r = row + dr
            c = column + dc

            if 0<= r < self.size and 0 <= c < self.size:

                case = self.get_case(r,c)

                if not case.is_empty() and case.get_contenu().color != color:

                    r += dr
                    c += dc

                    while 0 <= r < self.size and 0 <= c < self.size:

                        case = self.get_case(r,c)
                        if case.is_empty():
                            break
                        if case.get_contenu().color == color:
                            return True

                        r += dr
                        c += dc
        return False
        
        
    def cases_jouables(self, color):
        candidates = self.case_candidates(color)
        jouables = []

        for row, column in candidates:
            if self.move_jouable(row,column,color):
                jouables.append((row,column))
        return jouables


    def appliquer_flips(self, row, column, color):

        

        for dr, dc in self.DIRECTIONS:

            r = row + dr
            c = column + dc

            pawns_to_flip = []

            while 0 <= r < self.size and 0 <= c < self.size:

                case = self.get_case(r, c)

                if case.is_empty():
                    break

                pawn = case.get_contenu()

                if pawn.color == color:
                    if pawns_to_flip:
                        for pawn_to_flip in pawns_to_flip:
                            pawn_to_flip.flip()
                    break

                else:
                    pawns_to_flip.append(pawn)

                r += dr
                c += dc

