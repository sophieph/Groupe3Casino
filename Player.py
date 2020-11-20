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
                    'date', 'nom', 'niveau', 'solde_depart', 'solde_fin', 'nb_coup', 'gain', 'mise', 'perdu'
                     ]
                writer = csv.DictWriter(stat_file, fieldnames=fieldnames)
                writer.writeheader()
            
    # Methode pour sauvegarder les donnees
    def set_data_by_level(self, nb_coup, perdu):
        with open('stat.csv', "a", encoding="utf-8") as stat_file:
            stat_file.write(str(self.date) +
                ','+ str(self.nom) + 
                ','+ str(self.level.level) +
                ','+ str(self.solde_depart) +
                ','+ str(self.solde) +
                ','+ str(nb_coup) +
                ','+ str(self.gain) + 
                ','+ str(self.mise) +
                ','+ str(perdu) + '\n')

    
    #Methode qui decrit les stats du joueur
    def player_exists(self):
        with open('stat.csv', "r", encoding="utf-8") as stat_file:
            lines = stat_file.readlines()
            for i in lines:
                if (self.nom in i):
                    return True
            return False

    def get_stat(self, nom):
        with open('stat.csv', "r", encoding="utf-8") as stat_file:
            lines = stat_file.readlines()
            tmp = []
            for line in lines:
                if(nom in line):
                    tmp.append(line)
            return tmp

    def get_mise_max(self, nom):
        lines = self.get_stat(nom)
        mises = []
        for i in lines:
            mises.append(i.split(','))
        mise_max = int(mises[0][7])
        for i in range(1, len(mises)):
            if (mise_max < int(mises[i][7])):
                mise_max = int(mises[i][7])
        return mise_max

    def get_mise_min(self, nom):
        lines = self.get_stat(nom)
        mises = []
        for i in lines:
            mises.append(i.split(','))
        mise_max = int(mises[0][7])
        for i in range(1, len(mises)):
            if (mise_max > int(mises[i][7])):
                mise_max = int(mises[i][7])
        return mise_max
    
    def get_gain_max(self, nom):
        lines = self.get_stat(nom)
        gains = []
        for i in lines:
            gains.append(i.split(','))
        gain_max = int(gains[0][6])
        for i in range(1, len(gains)):
            if (gain_max < int(gains[i][6])):
                gain_max = int(gains[i][6])
        return gain_max

    def get_gain_min(self, nom):
        lines = self.get_stat(nom)
        gains = []
        for i in lines:
            gains.append(i.split(','))
        gain_max = int(gains[0][6])
        for i in range(1, len(gains)):
            if (gain_max > int(gains[i][6])):
                gain_max = int(gains[i][6])
        return gain_max

    def get_level_max(self, nom):
        lines = self.get_stat(nom)
        levels = []
        for i in lines:
            levels.append(i.split(','))
        level_max = int(levels[0][2])
        for i in range(1, len(levels)):
            if (level_max < int(levels[i][2])):
                level_max = int(levels[i][2])
        return level_max
    def get_premier(self, nom):
        lines = self.get_stat(nom)
        coups = []
        for i in lines:
            coups.append(i.split(','))
        cpt = 0
        for i in range(0, len(coups)):
            if (1 == int(coups[i][5])):
                cpt += 1
        return cpt

    def get_mise_moyenne(self, nom):
        lines = self.get_stat(nom)
        mises = [] 
        for i in lines :
            mises.append(i.split(','))
        moy = 0
        for i in range(0, len(mises)):
            moy += int(mises[i][7]) 
        return int(moy/len(mises))

    def get_gain_moyen(self, nom):
        lines = self.get_stat(nom)
        gains = [] 
        for i in lines :
            gains.append(i.split(','))
        moy = 0
        for i in range(0, len(gains)):
            moy += int(gains[i][6]) 
        return int(moy/len(gains))
    def get_gagner(self, nom):
        lines = self.get_stat(nom)
        tab = []
        for i in lines:
            tab.append(i.split(','))
        cpt = 0
        for i in range(0, len(tab)):
            if ("False" in  tab[i][8]):
                cpt += 1
        return cpt

    def get_perdre(self, nom):
        lines = self.get_stat(nom)
        tab = []
        for i in lines:
            tab.append(i.split(','))
        cpt = 0
        for i in range(0, len(tab)):
            if ("True" in  tab[i][8]):
                cpt += 1
        return cpt
