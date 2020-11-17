import random

class Niveau:
    """ 
    - level 
    - solde
    - nb_python
    - nb_user
    - mise
    """

    def __init__(self, level, solde ):
        self.level = level
        self.solde = solde
        self.nb_python = random.randrange(1, 10*level) 
        self.nb_user = 0
        self.mise = 0

    def set_nb_user(nombre):
        if (nombre >=0 and nombre <= (self.level*10)):
            self.nb_user = nombre
            return True
        else :
            return False

    def set_mise(n, mise):
        if(n <= self.solde):
            self.mise = n
            return True
        else :
            return False

    def nb_user_true():
         return (self.nb_user == self.nb_python)

    def get_level():
        return self.level

    def get_solde():
        return self.solde

    def get_nb_python():
        return self.nb_python

    def get_nb_user():
        return self.nb_user

    def get_mise():
        return self.mise
