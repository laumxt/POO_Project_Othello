from board import Board
from color import Color
from input import Input
from player import Player
from session import Session
from pawn import Pawn
from playerIA import PlayerIA

def afficher_score(session):
    scores = session.compter_pions()

    print("\n------ SCORE ------")
    print("Noir  :", scores[Color.Noir])
    print("Blanc :", scores[Color.Blanc])
    print("-------------------\n")

def choisir_joueur(couleur):
    print(f"\nChoisissez le type de joueur pour {couleur.name} :")
    print("1. Joueur humain")
    print("2. Joueur IA")

    while True:
        choix = input("Votre choix : ")

        if choix == "1":
            return Player(couleur)
        elif choix == "2":
            return PlayerIA(couleur)
        else:
            print("Choix invalide. Veuillez choisir 1 ou 2.")

def main():

#initialisation du plateau, du joueur, de l'input et de la session
    mon_board = Board()

# Placement des quatre pions de départ
    mon_board.get_case(3, 3).place_pawn(Pawn(Color.Blanc))
    mon_board.get_case(4, 4).place_pawn(Pawn(Color.Blanc))
    mon_board.get_case(3, 4).place_pawn(Pawn(Color.Noir))
    mon_board.get_case(4, 3).place_pawn(Pawn(Color.Noir))

    print("=== Configuration des joueurs ===")
    joueur_noir = choisir_joueur(Color.Noir)
    joueur_blanc = choisir_joueur(Color.Blanc)


#création de la session
    ma_session = Session(mon_board, joueur_noir, joueur_blanc)

#boucle de jeu
    while not ma_session.jeu_termine:

        #recuperation de la couleur du joueur dont c'est le tour
        couleur_tour_courant = ma_session.tour_joueur

        #affichage du plateau demandé à board
        mon_board.display()
        afficher_score(ma_session)

        #creation dun joueur du tour courant
        mon_joueur = ma_session.joueurs[couleur_tour_courant]

        #recuperation des coordonnées du coup à jouer
        print("C'est le tour du joueur de couleur :", couleur_tour_courant)
        if isinstance(mon_joueur, PlayerIA):
    # La IA choisit son coup
            x, y = mon_joueur.choisir_coup(mon_board)

        else:
            # Le joueur humain saisit les coordonnées
            mon_input = Input(mon_board, mon_joueur)
            mon_input.demander_coordonnees()
            x, y = mon_input.get_input()

        mon_board.placer_pion(x, y, couleur_tour_courant)
    

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


