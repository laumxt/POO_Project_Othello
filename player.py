from POO.Othello import board, session


class Player:
    def __init__(self, color, mon_tour=False):
        self.color = color
        self.mon_tour = mon_tour

    def tour(self):
        if self.mon_tour == session.Session.tour_joueur:
            if board.Board.move_jouable(self.color):
                self.mon_tour = True
            else:
                self.mon_tour = False
        