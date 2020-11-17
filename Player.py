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
        self.solde = ""
        self.level = 1

    #Methode qui set le nom du joueur
    def setNom(self, nom):
        self.nom = nom

        return self.nom

    # Methode qui set le level du joueur
    def setLevel(self, level):
        self.level = level
    
    # Methode qui set le solde de départ du joueur
    def setSoldeDepart(self, solde):
        error = "Le montant saisie n'est pas valide, solde minimum de 1€ requis : "
        try:
            solde = float(solde)
            if solde < 1:
                print(error)
            else:
                self.solde_depart = solde
                self.solde = solde

                return self.solde
        except ValueError:
            print(error)    

