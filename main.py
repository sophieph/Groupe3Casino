

name_user = input("Bonjour je suis Python. Quel est votre pseudo ? ")
print ("Hello "+name_user+", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.")
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
mise = input("Le jeu commence, entrez votre mise : ?")
while mise > 1:
    mise = input("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ? ")
    if mise == 0:
        print("Aurevoir")
        break

