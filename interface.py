from board import Board
from color import Color
from input import Input
from player import Player
from session import Session
from pawn import Pawn


def main():

#initialisation du plateau, du joueur, de l'input et de la session
    mon_board = Board()

# Placement des quatre pions de départ
    mon_board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
    mon_board.get_case(4, 4).place_pawn(Pawn(Color.Blanc))
    mon_board.get_case(3, 4).place_pawn(Pawn(Color.Noir))
    mon_board.get_case(4, 3).place_pawn(Pawn(Color.Noir))


#création de la session
    ma_session = Session(mon_board)

   

#boucle de jeu
    while not ma_session.jeu_termine:

        #recuperation de la couleur du joueur dont c'est le tour
        couleur_tour_courant = ma_session.tour_joueur

        #affichage du plateau demandé à board
        mon_board.display()

        #creation dun joueur du tour courant
        mon_joueur = Player(couleur_tour_courant, ma_session)

        #recuperation des coordonnées du coup à jouer
        print("C'est le tour du joueur de couleur :", couleur_tour_courant)
        mon_input = Input(mon_board, mon_joueur, mon_abscisse=None, mon_ordonnee=None)

        mon_input.demander_coordonnees()
        x,y = mon_input.get_input()

        #jouer le coup
        mon_board.jouer(x,y, couleur_tour_courant)

        #affichage du plateau demandé à board
        mon_board.display()

        #actualisation du tour
        ma_session.mettre_a_jour_tour()

#resultat final
    gagnant = ma_session.gagnant()
    if gagnant == Color.Blanc:
        print("Le joueur Blanc a gagné !")
    elif gagnant == Color.Noir:
        print("Le joueur Noir a gagné !")
    else:
        print("Match nul !")


#lancement du main si le fichier est exécuté directement
if __name__ == "__main__":
    main()


