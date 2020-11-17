# Class User 

class Player: 
    """Classe définissant un joueur caractérisée par :
    - son nom
    - son solde de départ
    - son solde actuel
    - son niveau maximum atteint pendant le jeu 
    """

    def __init__(self): # Notre méthode constructeur
        self.nom = ""
        self.solde_depart = 10
        self.solde = 10
        self.level = 1

    #Methode qui set le nom du joueur
    def set_nom(self, nom):
        self.nom = nom

        return self.nom

    # Methode qui set le level du joueur
    def set_level(self, level):
        self.level = level
    
    # Methode qui set le solde de départ du joueur
    def set_solde(self, solde):
        self.solde = solde
        return solde
        

