from board import Board
from color import Color
from input import Input
from session import Session


# à qui c'est le tour demandé à session
# affichage du plateau demandé à board
# où le joueur veut jouer demandé à input
# maj du plateau demandé à board
# est-ce que le jeu est terminé demandé à session
# si le jeu est pas terminé, maj du tour demandé à session


class Interface:
    def afficher_resultat(self, session: Session) -> None:
        if not session.jeu_termine:
            print("Le jeu n'est pas terminé.")
            return

        gagnant = session.gagnant()
        if gagnant == Color.Blanc:
            print("Le joueur Blanc a gagné !")
        elif gagnant == Color.Noir:
            print("Le joueur Noir a gagné !")
        else:
            print("Match nul !")
