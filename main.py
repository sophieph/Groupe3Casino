from Player import Player
from Niveau import Niveau
import sys
import select
from inputimeout import inputimeout, TimeoutOccurred

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def choice(value):
    if (value == "1"):
        return True
    elif (value == "2"):
        print('nom :   ' + player.nom)
        print('level : ' + str(player.level.get_level()))
        print('solde : ' + str(player.solde))
        print('gain  : ' + str(player.gain))
        print('mise  : ' + str(player.mise))
        #TODO : afficher statistiques avec bdd
        return True
    elif (value == "3"):
        print(regle)
        return True
    elif (value == "4"):
        print('Au revoir ! ')
        return False


name_user = input("Je suis Python. Quel est votre pseudo ? ")
player = Player(Niveau(1))
player.nom = name_user

# open the stat file if exists not create
filename = 'stat.csv'
player.open_file(filename)

print ("Hello " + player.nom + ", vous avez " + str(player.solde)+ " €, Très bien ! Installez vous SVP à la table de pari.")

regle="- Je viens de penser à un nombre entre 1 et " + str(player.level.get_level() * 10) + ". Devinez lequel ?\n\
- Att : vous avez le droit à trois essais !\n\
- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n\
- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n\
- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n\
- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et vous avez le droit :\n\
    - de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.\n\
    - de quitter le jeu.\n\
- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur."

jeu = None
perdu = False
menu = """
    Menu du jeu : \n
    \t 1) Lancer le jeu \n
    \t 2) Afficher les informations de la session \n
    \t 3) Afficher les règles \n
    \t 4) Quitter
"""
print(menu)
choice_user = input()

jeu = choice(choice_user)

if jeu:
    player.mise = input("Le jeu commence, entrez votre mise : ? ")

while jeu:
    while ( not player.level.mise_is_valid(player.mise, player.solde)):
        player.mise = input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et " + str(player.solde) + " € :  ? ")
        
    print("nb_python : "  + str(player.level.nb_python))
    nb_coup = player.level.get_nb_coup_max()
    player.mise = int(player.mise)
    player.set_solde(player.solde - player.mise)

    essai = 1
    
    while essai <= nb_coup:
        try:
            nb_user = inputimeout("mon nombre est : ? ", timeout = 10) 
        except TimeoutOccurred:
            reste = nb_coup - essai
            print("Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant et il vous reste " + str(reste) +" essai(s) !")
            essai += 1
            continue
            
        is_value = player.level.nb_user_is_valid(nb_user)        
        if is_value:
            nb_user = int(nb_user)
            if nb_user > player.level.nb_python:
                print("Votre nbre est trop grand !")
                reste = nb_coup - essai
                print(bcolors.FAIL +"Il vous reste " +  str(reste) + " chance !"+ bcolors.ENDC)
                essai += 1

            elif nb_user < player.level.nb_python:
                print("Votre nbre est trop petit !")
                reste = nb_coup - essai
                print(bcolors.FAIL + "Il vous reste " + str(reste) + " chance !" + bcolors.ENDC)
                essai += 1

            elif nb_user == player.level.nb_python:
                player.gain = int(player.level.get_gain(player.mise, essai))
                player.set_solde(player.solde + player.gain)
                print(bcolors.WARNING + "Bingo " + player.nom + ", vous avez gagné en " + str(essai) + " coup(s) et vous avez emporté " + str(player.gain) + " € !" + bcolors.ENDC)
                if (player.level.level != 3):
                    print("Super ! Vous passez au Level " + str(player.level.level + 1) + "! ")
                break
        else:
            print("Je ne comprends pas ! Entrez un nombre entre 1 et " + str(player.level.level * 10))
            reste = nb_coup - essai
            print(bcolors.FAIL + "Il vous reste " + str(reste) + " chance !" + bcolors.ENDC)
            essai += 1

        if essai > nb_coup and nb_user != player.level.nb_python:
            player.gain = player.gain = 0
            print(bcolors.FAIL + "Vous avez perdu ! Mon nombre est " + str(player.level.nb_python) + " !" + bcolors.ENDC)
            perdu = True
            

    player.set_data_by_level(essai)

    # si le joueur arrive au max level sans perdre
    if player.level.level == 3 and perdu == False:
        jeu = False
        print("Au revoir ! Vous finissez la partie avec "+ str(player.solde)+" €.")
        break
    else :
        if player.solde > 0:
            continuer = "" 
            try:
                continuer = inputimeout("Souhaitez-vous continuer la partie (O/N) ? ", timeout = 10)
            except TimeoutOccurred:
                jeu = False
                print("Au revoir ! Vous finissez la partie avec "+ str(player.solde)+" €.")
                break

            while True:
                if continuer == "O" or continuer == "o" :
                    if perdu:
                        if player.level.get_level() == 1:
                            player.level = Niveau(1)
                        elif player.level.get_level() != 1:
                            player.level = Niveau(player.level.level - 1)
                        perdu = False
                        break
                    else: 
                        if (player.level.level == 3):
                            jeu = False
                        player.level = Niveau(player.level.level + 1)
                    break
                elif continuer == "N" or continuer == "n" :
                    print("Au revoir ! Vous finissez la partie avec "+ str(player.solde)+ " €.")
                    jeu = False
                    break
                else:
                    try:
                        continuer = inputimeout("Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?", timeout = 10 )
                    except TimeoutOccurred:
                        jeu = False
                        print("Au revoir ! Vous finissez la partie avec "+ str(player.solde)+ " €.")
                        break 
        else:
            print("Vous n'avez plus rien, au revoir ! ")   
            jeu = False