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
solde = player.solde
#faire appel fonction mise

jeu = True

while jeu:
    nb_python = level.get_nb_python
    nb_coup = level.get_nb_coup_max()

    mise = input("Le jeu commence, entrez votre mise : ? ")
    while ( not level.mise_is_valid(mise, solde)):
        mise = input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ? ")
    
    player.add_mise(mise)

    nb_user = input("Alors mon nombre est : ? " )
    test = level.nb_user_is_valid(nb_user)
    essai = 1
    
    while essai < nb_coup or nb_user!=nb_python:

        if test:
            nb_user = level.nb_user_is_true()

            if nb_user > nb_python:
                print("Votre nbre est trop grand !")
                essai+1
                print("Il vous reste "+essai - nb_coup+" chance !")

            if nb_user < nb_python:
                print("Votre nbre est trop petit !")
                essai+1
                print("Il vous reste "+essai - nb_coup+" chance !")

            if nb_user == nb_python:
                print ("Bingo "+player.nom+", vous avez gagné en "+essai+" coup(s) et vous avez emporté "+gain+" € !")
                break
        else:
            nb_user = input("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?")
            essai+1


    if nb_user != nb_python:
        print("Vous avez perdu ! Mon nombre est "+nb_python+" !")
        perdu = True

    continuer = input("Souhaitez-vous continuer la partie (O/N) ? ")

    while continuer != "O" or "o" or "N" or "n":
        continuer = input("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?" )

    if continuer == "O" or "o" :
        if perdu and level.get_level() != 1:
            level=Niveau(level.get_level() - 1)
            
        
        elif perdu and level.get_level() == 1:
            level=Niveau(1)
        
        else:
            level=Niveau(level.get_level() + 1)
        
        player.set_level(level)
        
    if continuer == "N" or "n" :
        print("Au revoir ! Vous finissez la partie avec "+gain+" €.")
        jeu = False
        
