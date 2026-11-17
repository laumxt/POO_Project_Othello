from board import Board
from pawn import Pawn
from color import Color
from playerIA import PlayerIA

# board = Board()

# board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
# board.get_case(3, 4).place_pawn(Pawn(Color.Noir))
# board.get_case(4, 4).place_pawn(Pawn(Color.Blanc))
# board.get_case(4, 3).place_pawn(Pawn(Color.Noir))

# board.display()

# print(board.cases_jouables(Color.Blanc))

#initialisation du plateau, du joueur, de l'input et de la session
mon_board = Board()

# Placement des quatre pions de départ
mon_board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
mon_board.get_case(4, 4).place_pawn(Pawn(Color.Blanc))
mon_board.get_case(3, 4).place_pawn(Pawn(Color.Noir))
mon_board.get_case(4, 3).place_pawn(Pawn(Color.Noir))

mon_board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
mon_board.get_case(3, 4).place_pawn(Pawn(Color.Noir))

mon_board.display()
mon_board.placer_pion(3, 5, Color.Blanc)

ia = PlayerIA(Color.Noir)
coup = ia.choisir_coup(mon_board)

print(coup)