import random

class Niveau:
    """ 
    - level 
    - solde
    - nb_python
    - nb_user
    - mise
    """

    def __init__(self, level):
        self.level = level
        self.nb_python = random.randrange(1, 10*level) 
        
    def set_nb_user(self, nombre):
        if (nombre >=0 and nombre <= (self.level*10)):
            self.nb_user = nombre
            return True
        else :
            return False  

    def set_mise(self, n,  solde):
        if(n <= solde):
            self.mise = n
            return True
        else :
            return False

    def nb_user_true(self):
         return (self.nb_user == self.nb_python)

    def get_level(self):
        return self.level

    def get_nb_python(self):
        return self.nb_python

    def get_nb_user(self):
        return self.nb_user

    def get_mise(self):
        return self.mise
