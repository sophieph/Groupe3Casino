import random

class Niveau:
    """ 
    - level 
    - nb_python
    """

    def __init__(self, level):
        self.level = level
        self.nb_python = random.randrange(1, 10*level)

    def get_level():
        return self.level

    def get_nb_python():
        return self.nb_python 

    def set_level(l):
        self.level = l

    def set_nb_python(n):
        self.nb_python = n

    def nb_user_is_valid(nombre):
        if (type(nombre) == int):
            if (nombre >=0 and nombre <= (self.level*10)):
                return True
            else:
                return False
        else :
            return False

    def nb_user_is_true(nombre, nb_user):
        return (nombre == nb_user)

    def mise_is_valid(mise, solde):
        if (type(mise) == int):
            if (mise >=0 and mise <= solde):
                return True
            else:
                return False
        else:
            return False

