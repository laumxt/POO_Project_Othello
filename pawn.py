from enum import Enum

class Color(Enum):
    Blanc = 0
    Noir = 1

class Pawn:
    def __init__(self, arg_color):
        self.color = arg_color

    def get_color(self):
        return self._color 

    def set_color(self, arg_color):
        if isinstance(arg_color, Color):
            self._color = arg_color
        else:
            raise ValueError("La couleur doit être une instance de Color")

    color = property(get_color, set_color)

    def flip(self):
        if self._color == Color.Blanc:
            self._color = Color.Noir
        else:
            self._color = Color.Blanc


test_pawn = Pawn(Color.Blanc)
print(f"Couleur initiale du pion : {test_pawn.color}")
print(f"Couleur initiale du pion : {test_pawn.color.name}")
test_pawn.flip()
print(f"Couleur après le flip : {test_pawn.color.name}")