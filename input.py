from player import Player
from board import Board
class Input:

    def __init__(self, monboard, monjoueur, mon_abscisse=None, mon_ordonnee=None):
        self._board = monboard
        self._joueur = monjoueur
        if mon_abscisse is not None and mon_ordonnee is not None:
            self.input = (mon_abscisse, mon_ordonnee)
        else:
            self._abscisse = None
            self._ordonnee = None

#saisie des coordonnées par l'utilisateur 
    def demander_coordonnees(self):
        while True:
            try:
                saisie = input("Entre les coordonnées (x,y) : ")
                coordonnees = [c.strip() for c in saisie.split(",")]
                if len(coordonnees) != 2:
                    raise ValueError("Veuillez entrer deux coordonnées séparées par une virgule.")
                elif not all(c.isdigit() for c in coordonnees):
                    raise ValueError("Veuillez entrer des nombres valides pour les coordonnées.")
                elif int(coordonnees[0])<0 or int(coordonnees[1])<0 or int(coordonnees[0])>7 or int(coordonnees[1])>7:
                    raise ValueError("Veuillez entrer des coordonnées entre 0 et 7.")
                else:
                    # Appelle le setter, met à jour l'attribut input avec un tuple
                    # permet de lancer les vérifications du setter pour s'assurer que les coordonnées sont valides
                    self.input = (int(coordonnees[0]), int(coordonnees[1]))  
                    return self
            except (ValueError, TypeError) as erreur:
                print(erreur)
    
        

    def get_input(self):
        return self._abscisse, self._ordonnee

    
    #le setter vérifie que les coordonnées sont valides et que le coup est jouable pour le joueur
    def set_input(self, coordonnees: tuple): 
        monboard = self._board 
        monjoueur = self._joueur
        if(
            isinstance(coordonnees, tuple) 
            and len(coordonnees) == 2 
            and isinstance(coordonnees[0], int) and isinstance(coordonnees[1], int) 
            and int(coordonnees[0])>=0 and int(coordonnees[1])>=0 
            and int(coordonnees[0])<=7 and int(coordonnees[1])<=7
        ):
            if (monboard.move_jouable(coordonnees[0], coordonnees[1], monjoueur.color)):
                self._abscisse = int(coordonnees[0])
                self._ordonnee = int(coordonnees[1])
            else:
                raise ValueError("Le coup n'est pas jouable pour le joueur de couleur " + monjoueur.color)
        
        else: raise TypeError("Les coordonnées doivent être un tuple de deux entiers entre 0 et 7.")

    #on ne peut lire ou modifier input que depuis get et set
    input = property(get_input, set_input) 



        