from board import Board
from pawn import Pawn
from color import Color

# board = Board()

# board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
# board.get_case(3, 4).place_pawn(Pawn(Color.Noir))
# board.get_case(4, 4).place_pawn(Pawn(Color.Blanc))
# board.get_case(4, 3).place_pawn(Pawn(Color.Noir))

# board.display()

# print(board.cases_jouables(Color.Blanc))

board = Board()

board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
board.get_case(3, 4).place_pawn(Pawn(Color.Noir))

board.display()
board.jouer(3, 5, Color.Blanc)

board.display()