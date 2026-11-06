from board import Board
from color import Color
from input import Input
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



#class Interface:
#    def afficher_resultat(self, session: Session) -> None:
  #      if not session.jeu_termine:
  #          print("Le jeu n'est pas terminé.")
   #         return


     #   gagnant = session.gagnant()
      #  if gagnant == Color.Blanc:
      #      print("Le joueur Blanc a gagné !")
       # elif gagnant == Color.Noir:
       #     print("Le joueur Noir a gagné !")
       # else:
        #    print("Match nul !")

