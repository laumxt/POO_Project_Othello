from pawn import Pawn
from player import Player
from color import Color
from session import Session
from board import Board
from interface import Interface


test_pawn = Pawn(Color.Blanc)
print(f"Couleur initiale du pion : {test_pawn.color}")
print(f"Couleur initiale du pion : {test_pawn.color.name}")
test_pawn.flip()
print(f"Couleur après le flip : {test_pawn.color.name}")


test_player=Player("black", True)
print(test_player.color)
Session.tour_joueur = True
Board.move_jouable = lambda color: True  # Mocking the method for testing
print(test_player.mon_tour)



test_session = Session(Board())
tour_joueur = test_session.tour_joueur
print(f"Tour du joueur : {tour_joueur.name}")

test_board = Board()
# Test case_candidates method
candidates = test_board.case_candidates(Color.Blanc)
print("Candidates for Blanc:", candidates)

test_session = Session(test_board)
# Test compter_pions method
scores = test_session.compter_pions()
print("Scores:", scores)    
test_session.mettre_a_jour_tour()
print(f"Tour du joueur après mise à jour : {test_session.tour_joueur.name}")
print(f"Jeu terminé : {test_session.jeu_termine}")
print(f"Gagnant : {test_session.gagnant()}")

test_affichage = Interface()
test_affichage.afficher_resultat(test_session)

test_board.display()
