import csv
from datetime import date
from datetime import datetime
import os.path
from os import path
import re
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
        self.id = 1
        self.nom = ""
        self.date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.solde_depart = 10
        self.solde = 10
        self.level = level
        self.nb_user = 0
        self.gain = 0
        self.mise = 0
        

    #Methode qui set le nom du joueur
    def set_nom(self, nom):
        self.nom = nom

        return self.nom
    
    # Methode qui set le level du joueur
    def set_level(self, level):
        self.level = level

        return self.level

    def set_nb_user(self, nb_user):
        self.nb_user = nb_user

        return self.nb_user
        
    def set_mise(self, mise):
        self.mise = mise
        
        return self.mise
    
    def set_gain(self, gain):
        self.gain = gain
        
        return self.gain

    # Methode qui set le solde de départ du joueur
    def set_solde(self, solde):
        self.solde = solde

        return solde

    # Methode pour creer un fichier
    def open_file(self, filename):
        if not path.exists(filename):
            with open(filename, 'w+') as stat_file:
                fieldnames = [
                    'id', 'date', 'nom', 'niveau', 'solde_depart', 'solde_fin', 'nb_coup', 'gain', 'mise', 
                     ]
                writer = csv.DictWriter(stat_file, fieldnames=fieldnames)
                writer.writeheader()
            
    # Methode pour sauvegarder les donnees
    def set_data_by_level(self, nb_coup):
        with open('stat.csv', "a", encoding="utf-8") as stat_file:
            stat_file.write(str(self.id) +
             ',' + str(self.date) +
              ',' + str(self.nom) + 
              ','+ str(self.level.level) +
               ','+ str(self.solde_depart) +
                ','+ str(self.solde) +
                ','+ str(nb_coup) +
                 ','+ str(self.gain) + ','+ str(self.mise) + '\n')

    
    # Methode si le joueur existe
    def player_exists(self):
        with open('stat_niveau.csv', "r", encoding="utf-8") as stat_file:
            for line in stat_file:
                match = re.search(self.nom, line)
                if match:
                    return True
                else: 
                    return False

    #Methode qui decrit les stats du joueur
    # def show_stat():