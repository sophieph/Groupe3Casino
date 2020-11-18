from math import *
import random

# Argent de départ fixé
argent=10000000

# Mise sur un numéro
mise_numero=input("Veuillez svp miser sur un numéro compris entre 0 et 49 : ")
try:
	mise_numero=int(mise_numero)
except ValueError:
	print("La valeur saisie n'est pas un entier.")
except TypeError:
	print("La valeur saisie n'est pas un entier.")
while mise_numero<0 or mise_numero>49:
	mise_numero=input("Veuillez svp miser sur un numéro compris entre 0 et 49 : ")
	try:
		mise_numero=int(mise_numero) 
	except ValueError:
		print("La valeur saisie est soit négative soit supérieure à 49.")		

# Mise argent
mise_argent=input("\nVeuillez svp miser l'argent que vous désirez($) : ")
try:
	mise_argent=int(mise_argent)
except ValueError:
	print("La valeur saisie n'est pas un entier.")
except TypeError:
	print("La valeur saisie n'est pas un entier.")
while mise_argent<0:
	mise_argent=input("Veuillez svp miser l'argent que vous désirez($) : ")
	try:
		mise_argent=int(mise_argent) 
	except ValueError:
		print("La valeur saisie est sûrement négative.")
argent=argent-mise_argent

# Roulette
numero_gagnant=random.randrange(50)
r=numero_gagnant%2
if r==0:
	couleur_gagnante="noir"
else:
	couleur_gagnante="rouge"

# Numéro misé pair(noir) ou impair(rouge)
if mise_numero%2==0:
	couleur="noir"
else:
	couleur="rouge"

# Affichage du numéro gagnant
print("\nLe numéro gagnant était ", numero_gagnant,".")

# Résultats
if mise_numero==numero_gagnant:
	argent=argent+mise_argent+(mise_argent*3)
	print("\nFélicitations!!! Vous avez trouvé le numéro gagnant.")
elif couleur==couleur_gagnante:
	argent=argent+mise_argent+(ceil(mise_argent/2))
	print("\nVous n'avez pas trouvé le numéro gagnant mais votre numéro était de la même couleur (",couleur_gagnante,").")
else:
	pass
print("\nVotre argent à la fin du jeu est : ", argent,".")
