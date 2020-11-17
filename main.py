print('Hello world')
from random import randint
from Niveau import Niveau 
from Player import Player

niveau = Niveau(1, 1)
sophie = Player(niveau)

print(sophie.level.level)