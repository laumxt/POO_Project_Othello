from board import Board
from session import Session
from input import Input
from color import Color
from player import Player


def main():

#initialisation du plateau, du joueur, de l'input et de la session
    mon_board = Board()
#les noirs commencent
    mon_joueur = Player(Color.Noir, Session(mon_board))
    mon_input = Input(mon_board, mon_joueur, mon_abscisse=None, mon_ordonnee=None)
    ma_session = Session(mon_board)

#boucle de jeu
    while not ma_session.jeu_termine:
        couleur_tour_courant = ma_session.tour_joueur()
        print("C'est le tour du joueur de couleur :", couleur_tour_courant)
        #affichage du plateau demandé à board
        mon_board.afficher_plateau()
        mon_input.demander_coordonnees()
        mon_board.jouer(mon_input.input)
        #affichage du plateau demandé à board
        mon_board.afficher_plateau()
        ma_session.mettre_a_jour_tour()

    print("Le jeu est terminé !")

#où le joueur veut jouer demandé à input

demander_coordonnees = mon_input.demander_coordonnees()

input_accepte = mon_input.input

#maj du plateau demandé à board

maj_plateau = mon_board.jouer(demander_coordonnees)

#nouvel affichage du plateau demandé à board

display_board_maj = mon_board.afficher_plateau()


#si le jeu est pas terminé, maj du tour demandé à session

maj_tour = ma_session.mettre_a_jour_tour()