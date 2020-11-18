from Player import Player
from Niveau import Niveau
import sys
import select

class TimeoutExpired(Exception):
    pass

# Créer une limite de temps à l'input
def input_with_timeout(prompt, timeout):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n')  # expect stdin to be line-buffered
    raise TimeoutExpired


level = Niveau(1)
name_user = input("Bonjour je suis Python. Quel est votre pseudo ? ")
player = Player(level)
player.nom = name_user

print ("Hello " + player.nom + ", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.")
regle="- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n\
- Att : vous avez le droit à trois essais !\n\
- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n\
- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n\
- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n\
- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et vous avez le droit :\n\
    - de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.\n\
    - de quitter le jeu.\n\
- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur."
#print(regle)

jeu = True
perdu = False

while jeu:
    nb_python = level.get_nb_python()
    print(nb_python)
    nb_coup = level.get_nb_coup_max()

    mise = input("Le jeu commence, entrez votre mise : ? ")
    while ( not level.mise_is_valid(mise, player.solde)):
        mise = input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ? ")
    
    mise=int(mise)
    player.add_mise(mise)
    player.set_solde(player.solde - mise)

    nb_user = input("Alors mon nombre est : ? " )
    essai = 1

    test = level.nb_user_is_valid(nb_user)
    print(nb_python)
    while essai < nb_coup:
        test = level.nb_user_is_valid(nb_user)
        nb_user=int(nb_user)
        
        if test:            
            if nb_user > nb_python:
                print("Votre nbre est trop grand !")
                reste = nb_coup - essai
                print("Il vous reste "+  str(reste) +" chance !")
                essai += 1

            elif nb_user < nb_python:
                print("Votre nbre est trop petit !")
                reste = nb_coup - essai
                print("Il vous reste "+ str(reste) +" chance !")
                essai += 1

            elif nb_user == nb_python:
                gain = level.get_gain(mise, essai)
                player.set_solde(player.solde + gain)
                player.add_gain(gain)

                print ("Bingo "+player.nom+", vous avez gagné en "+ str(essai) +" coup(s) et vous avez emporté "+ str(gain) +" € !")
                break
        else:
            # nb_user = input("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?")
            essai+=1

        nb_user=input("Nombre ? ")


    if nb_user != nb_python:
        print("Vous avez perdu ! Mon nombre est "+ str(nb_python)+" !")
        perdu = True

    continuer = input("Souhaitez-vous continuer la partie (O/N) ? ")

    while True:
        if continuer == "O" or continuer == "o" :
            if perdu and level.get_level() != 1:
                level=Niveau(level.get_level() - 1)
                break
        
            elif perdu and level.get_level() == 1:
                level=Niveau(1)
                break

            else:
                level=Niveau(level.get_level() + 1)
            
            player.set_level(level)
            break
        elif continuer == "N" or continuer == "n" :
            print("Au revoir ! Vous finissez la partie avec "+ str(gain)+" €.")
            jeu = False
            player.set_level(level)
            break
       
        continuer = input("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?" )
        continue