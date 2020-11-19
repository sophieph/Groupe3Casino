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


filename = 'stat.csv'

level = Niveau(1)
name_user = input("Bonjour je suis Python. Quel est votre pseudo ? ")
player = Player(level)
player.nom = name_user

#Check if file exists
player.open_file(filename)

print ("Hello " + player.nom + ", vous avez " + str(player.solde)+ " €, Très bien ! Installez vous SVP à la table de pari.")
regle="- Je viens de penser à un nombre entre 1 et " + str(player.level.get_level()*10) + ". Devinez lequel ?\n\
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

    player.mise = input("Le jeu commence, entrez votre mise : ? ")
    while ( not level.mise_is_valid(player.mise, player.solde)):
        player.mise = input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ? ")
    
    nb_python = level.get_nb_python()
    nb_coup = level.get_nb_coup_max()

    player.mise = int(player.mise)
    player.set_solde(player.solde - player.mise)

    essai = 1
    exception = True
   
    print("nb_python : " + str(player.level.nb_python))
    while essai <= nb_coup:
        # TimeoutException
        try:
            player.nb_user = int(input("mon nombre est : ? ")) 
        except TimeoutExpired:
            print('\nVous avez mis trop de temps pour repondre, vous perdez un coup ...\n')
            reste = nb_coup - essai
            print("Il vous reste "+  str(reste) +" chance !")
            essai += 1
            continue
        
        test = player.level.nb_user_is_valid(player.nb_user)        
        if test:            
            player.nb_user = int(player.nb_user)
            if player.nb_user > player.level.nb_python:
                print("Votre nbre est trop grand !")
                reste = nb_coup - essai
                print("Il vous reste "+  str(reste) +" chance !")
                essai += 1

            elif player.nb_user < player.level.nb_python:
                print("Votre nbre est trop petit !")
                reste = nb_coup - essai
                print("Il vous reste "+ str(reste) +" chance !")
                essai += 1

            elif player.nb_user == player.level.nb_python:
                player.gain = level.get_gain(player.mise, essai)
                print(player.gain)
                player.set_solde(player.solde + player.gain)
                print(player.solde)

                print ("Bingo " + player.nom + ", vous avez gagné en "+ str(essai) +" coup(s) et vous avez emporté "+ str(player.gain) +" € !")
                break
        else:
            nb_user = input("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?")
            essai+=1

    if player.nb_user != player.level.nb_python:
        print("Vous avez perdu ! Mon nombre est "+ str(player.level.nb_python) +" !")
        perdu = True

    player.set_data_by_level(essai)    

    continuer = "" 
    # exception
    try:
        continuer = input("Souhaitez-vous continuer la partie (O/N) ? ")
    except TimeoutExpired:
        jeu = False
        break

    while True:
        if continuer == "O" or continuer == "o" :
            if perdu and player.level.get_level() != 1:
                player.level = Niveau(player.level.get_level() - 1)
                break
            elif perdu and player.level.get_level() == 1:
                player.level = Niveau(1)
                break
            else:
                player.level = Niveau(level.get_level() + 1)

            level = Niveau(level.get_level() + 1)        
            player.set_level(level)
            break

        elif continuer == "N" or continuer == "n" :
            print("Au revoir ! Vous finissez la partie avec "+ str(player.gain) +" €.")
            jeu = False
            player.set_level(level)
            break
        # exception
        try:
            continuer = input("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?")
        except TimeoutExpired:
            jeu = False
            break 
