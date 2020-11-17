# Class User 

class Player: 
    """Classe définissant un joueur caractérisée par :
    - son nom
    - son solde de départ
    - son solde de fin de jeu
    - son niveau maximum atteint pendant le jeu 
    - son lieu de résidence"""

    
    def __init__(self): # Notre méthode constructeur
        self.nom = ""
        self.solde_depart = ""
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

    # Methode qui retourne le solde selon la mise
    def setSoldeAvecMise(self, mise):
        mise_min = 0.01
        try:
            mise = int(mise)
            if (mise < mise_min):
                print(
                    "Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et %.2d € :" % (self.solde))
            elif mise > int(self.solde):
                print("Erreur, votre mise est plus elevé que votre solde.\n")
                print("Entrez une mise inférieur ou égale à %.2d € :" % (self.solde))
            else: 
                self.solde -= mise

                return self.solde

        except ValueError:
            print("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et %.2d € : " % (self.solde))





    

