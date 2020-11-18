import csv
from datetime import date

from Niveau import Niveau

# Class User 
class Player: 
    """Classe définissant un joueur caractérisée par :
    - son nom
    - son solde de départ
    - son solde actuel
    - son niveau maximum atteint pendant le jeu  - Objet Niveau
    """

    def __init__(self, level): # Notre méthode constructeur
        self.nom = ""
        self.date = date.today()
        self.solde_depart = 10
        self.solde = 10
        self.level = level
        self.gain = []
        self.mise = []
        self.gain_max = 0
        self.mise_max = 0
        

    #Methode qui set le nom du joueur
    def set_nom(self, nom):
        self.nom = nom

        return self.nom
    

    # Methode qui set le level du joueur
    def set_level(self, level):
        self.level = level

        return self.level
    
    # Methode qui set le solde de départ du joueur
    def set_solde(self, solde):
        self.solde = solde

        return solde

    # Methode qui ajoute le gain dans la liste Gain
    def add_gain(self, gain):
        self.gain.append(gain)
        for i in self.gain:
            if (i > self.gain_max):
                self.gain_max = i

    # Methode qui ajoute la mise dans la liste Mise
    def add_mise(self, mise):
        self.mise.append(mise)
        for i in self.mise:
            if (i > self.mise_max):
                self.mise_max = i

