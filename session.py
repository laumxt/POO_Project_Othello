from typing import Optional

from board import Board
from color import Color


class Session:
    def __init__(self, board: Board):
        self.board = board
        self.tour_joueur = Color.Blanc
        self.jeu_termine = False

    def mettre_a_jour_tour(self) -> None:
        if self.jeu_termine:
            return

        blanc_cases_jouables = bool(self.board.cases_jouables(Color.Blanc))
        noir_cases_jouables = bool(self.board.cases_jouables(Color.Noir))

        if not blanc_cases_jouables and not noir_cases_jouables:
            self.jeu_termine = True
            return

        if self.tour_joueur == Color.Blanc:
            self.tour_joueur = (
                Color.Noir if noir_cases_jouables else Color.Blanc
            )
        else:
            self.tour_joueur = (
                Color.Blanc if blanc_cases_jouables else Color.Noir
            )

    def compter_pions(self) -> dict[Color, int]:
        scores = {Color.Blanc: 0, Color.Noir: 0}
        for ligne in self.board.cases:
            for case in ligne:
                pion = case.get_contenu()
                if pion is not None:
                    scores[pion.color] += 1
        return scores

    def gagnant(self) -> Optional[Color]:
        if not self.jeu_termine:
            return None

        scores = self.compter_pions()
        score_blanc = scores[Color.Blanc]
        score_noir = scores[Color.Noir]

        if score_blanc > score_noir:
            return Color.Blanc
        if score_noir > score_blanc:
            return Color.Noir
        return None