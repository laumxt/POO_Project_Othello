from color import Color

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
