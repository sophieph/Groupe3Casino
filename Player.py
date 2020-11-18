import csv
from datetime import date
import os.path
from os import path
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
        self.date = date.today()
        self.solde_depart = 10
        self.solde = 10
        self.level = level
        self.nb_user = 0
        self.gain = 0
        self.mise = 0
        self.gainList = []
        self.miseList = []
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

    def set_nb_user(self, nb_user):
        self.nb_user = nb_user

        return self.nb_user
    def set_mise(self, mise):
        self.mise = mise
        
        return self.mise
    
    # Methode qui set le solde de départ du joueur
    def set_solde(self, solde):
        self.solde = solde

        return solde

    # Methode qui ajoute le gain dans la liste Gain
    def add_gain(self, gain):
        self.gainList.append(gain)
        for i in self.gainList:
            if (i > self.gain_max):
                self.gain_max = i

    # Methode qui ajoute la mise dans la liste Mise
    def add_mise(self, mise):
        self.miseList.append(mise)
        for i in self.miseList:
            if (i > self.mise_max):
                self.mise_max = i

    # Methode pour creer un fichier
    def open_file(self, filename):
        if not path.exists(filename):
            with open(filename, 'w+') as stat_file:
                fieldnames = [
                    'id', 'date', 'nom', 'niveau_max', 'solde_depart', 'solde_fin', 'liste_gain', 'liste_mise', 'gain_max', 'mise_max'
                     ]
                writer = csv.DictWriter(stat_file, fieldnames=fieldnames)
                writer.writeheader()
            
            with open('stat_niveau.csv', 'w+') as stat_niveau_file:
                fieldnames= [
                    'id_jeu', 'niveau', 'gain', 'nb_coup', 'mise'
                     ]
                writer_data = csv.DictWriter(stat_niveau_file, fieldnames=fieldnames)
                writer_data.writeheader()
        
    # Methode pour sauvegarder les donnees
    def set_data(self, filename):
        with open(filename, "a", encoding="utf-8") as stat_file:
            
            stat_file.write(str(self.id) +
             ',' + str(self.date) +
              ',' + str(self.nom) + 
              ','+ str(self.level.level) +
               ','+ str(self.solde_depart) +
                ','+ str(self.solde) +
                 ','+ str(self.gainList) + ','+ str(self.miseList) + ','+ str(self.gain_max) + ','+ str(self.mise_max) + '\n')