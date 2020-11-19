import random

class Niveau:
    """ 
    - level 
    - nb_python
    """

    def __init__(self, level):
        self.level = level
        self.nb_python = random.randrange(1, 10*level)
        print(self.nb_python)

    def get_level(self):
        return self.level

    def get_nb_python(self):
        return self.nb_python 

    def set_level(self, l):
        self.level = l

    def set_nb_python(self,n):
        self.nb_python = n
    def nb_user_is_valid(self, nombre):
        try:
            nombre = int(nombre)
            if (nombre > 0 and nombre <= (self.level*10)):
                return True
            else:
                return False
        except ValueError:
            return False

    def nb_user_is_true(self, nb_user):
        return (self.nb_python == nb_user)

    def mise_is_valid(self, mise, solde):
        try:
            mise = int(mise)
            if (type(mise) == int):
                if (mise > 0 and mise <= solde):
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            return False
        
    def get_nb_coup_max(self):
        if(self.level == 1):
            return 3
        elif (self.level == 2):
            return 5
        elif (self.level  == 3):
            return 7
    
    # update the get_gain function 
    def get_gain(self, mise, nb_essai):
        if (self.level == 1):
            if (nb_essai == 1):
                return 2*mise
            elif (nb_essai == 2):
                return mise
            elif (nb_essai == 3):
                return int(mise/2)
        elif(self.level == 2):
            if (nb_essai == 1):
                return 2*mise
            elif (nb_essai == 2 or nb_essai == 3):
                return mise
            elif (nb_essai == 4 or nb_essai == 5):
                return int(mise/2)
        elif(self.level == 3):
            if (nb_essai == 1):
                return 2*mise
            elif (nb_essai == 2 or nb_essai == 3 or nb_essai == 4):
                return mise
            elif (nb_essai == 5 or nb_essai == 6 or nb_essai == 7):
                return int(mise/2)

    def update_nb_python(self):
        self.nb_python = random.randrange(1, 10*level)

