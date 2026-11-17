from player import Player
import random

class PlayerIA(Player):

    def choisir_coup(self, board):
        coups = board.cases_jouables(self.color)

        if not coups:
            return None

        return random.choice(coups)