from Player import Player
from Niveau import Niveau

level=Niveau(1)
name_user = input("Bonjour je suis Python. Quel est votre pseudo ? ")
player = Player(level)
player.nom = name_user

print ("Hello "+player.nom+", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.")
regle="- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n\
- Att : vous avez le droit à trois essais !\n\
- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n\
- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n\
- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n\
- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et vous avez le droit :\n\
    - de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.\n\
    - de quitter le jeu.\n\
- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur."
print(regle)
player.solde_depart=10
#faire appel fonction mise
print("Le jeu commence, entrez votre mise : ? ")
mise = player.setSoldeAvecMise()

nb_python = niveau.get_nb_python

nb_user = input("Alors mon nombre est : ? " )
test = niveau.nb_user_is_valid(nb_user)

essaie = 1
gain=10
while essaie != 3 or nb_user!=nb_python:

    if test:
        nb_user = niveau.nb_user_is_true()

        if nb_user > nb_python:
            print("Votre nbre est trop grand !")
            essaie+1
            print("Il vous reste "+essaie - 3+" chance !")

        if nb_user < nb_python:
            print("Votre nbre est trop petit !")
            essaie+1
            print("Il vous reste "+essaie -3+" chance !")

        if nb_user == nb_python:
            print ("Bingo "+name_user+", vous avez gagné en "+essaie+" coup(s) et vous avez emporté "+gains+" € !")
            break
    else:
        nb_user = int(input("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?"))

if nb_user != nb_python:
    print("Vous avez perdu ! Mon nombre est "+nb_python+" !")

continuer = input("Souhaitez-vous continuer la partie (O/N) ? ")

while continuer != "O" or "o" or "oui" or "Oui" or "N" or "n" or "non" or "Non":
    continuer=(input("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?" ))

if continuer == "O" or "o" or "oui" or "Oui":
    print("Super !")

if continuer == "N" or "n" or "non" or "Non":
    print("Au revoir ! Vous finissez la partie avec "+gain+" €.")
    quit
