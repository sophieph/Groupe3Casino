from Player import Player
from Niveau import Niveau
import sys
import select

from inputimeout import inputimeout, TimeoutOccurred




name_user = input("Bonjour je suis Python. Quel est votre pseudo ? ")
player = Player(Niveau(1))
player.nom = name_user



# open the stat file
filename = 'stat.csv'
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

while jeu and (player.solde > 0):
    print('Menu du jeux : ')
    print('1) lancer le jeu')
    print('2) afficher les information de la session')
    print('3) afficher les regles')
    choix = input()
    if (choix == 3):
        print(regle)
    elif (choix == 2):
        print('nom :   ' + player.nom)
        print('level : ' + str(player.level.get_level()))
        print('solde : ' + str(player.solde))
        print('gain  : ' + str(player.gain))
        print('mise  : ' + str(player.mise))
    elif (choix == 1):
    player.mise = input("Le jeu commence, entrez votre mise : ? ")
    while ( not player.level.mise_is_valid(player.mise, player.solde)):
        player.mise = input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et " + str(player.solde) + " € :  ? ")
    
    print("nb_python : "  + str(player.level.nb_python))
    nb_coup = player.level.get_nb_coup_max()
    player.mise=int(player.mise)
    player.set_solde(player.solde - player.mise)

    essai = 1
    exception = True
   
    while essai <= nb_coup:
        # TimeoutException
        try:
            player.nb_user = inputimeout("mon nombre est : ? ", timeout = 20-(5*player.level.get_level())) 
        except TimeoutOccurred:
            print('\nVous avez mis trop de temps pour repondre, vous perdez un coup ...\n')
            essai += 1
            continue
        
        test = player.level.nb_user_is_valid(player.nb_user)        
        if test:            
            player.nb_user=int(player.nb_user)
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
                player.gain = int(player.level.get_gain(player.mise, essai))
                player.set_solde(player.solde + player.gain)
                print ("Bingo "+player.nom+", vous avez gagné en "+ str(essai) +" coup(s) et vous avez emporté "+ str(player.gain) +" € !")
                break
        else:
            print("Je ne comprends pas ! ")
            essai+=1

    if player.nb_user != player.level.nb_python:
        print("Vous avez perdu ! Mon nombre est "+ str(player.level.nb_python)+" !")
        perdu = True

    player.set_data_by_level(essai)
 
    continuer = "" 
    # exception
    if (player.level.get_level() != 3 and player.solde > 0):
        try:
            continuer = inputimeout("Souhaitez-vous continuer la partie (O/N) ? ", timeout= 10)
        except TimeoutOccurred:
            jeu = False
            break

        while True:
            if continuer == "O" or continuer == "o" :
                if perdu and player.level.get_level() != 1:
                    player.level=Niveau(player.level.get_level() - 1)
                    break
                elif perdu and player.level.get_level() == 1:
                    player.level=Niveau(1)
                    break
                else:
                    if player.level.get_level() == 3:
                        jeu = False
                        break
                    else: 
                        player.level=Niveau(player.level.get_level() + 1)
            
                break

            elif continuer == "N" or continuer == "n" :
                print("Au revoir ! Vous finissez la partie avec "+ str(player.gain)+" €.")
                jeu = False
                player.set_level(player.level)
                break
            # exception
       
            try:
                continuer = inputimeout("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?", timeout = 10 )
            except TimeoutOccurred:
                jeu = False
                break 
    else:
        jeu = False

print('\nLa fin du jeu, bye')
