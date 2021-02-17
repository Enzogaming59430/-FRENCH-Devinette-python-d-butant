from random import randint
import math
a = randint(1, 100)
print()
print('/--------------o')
print('|   Devinette  |')
print('| BETA 1.4.9   |')
print('|  [Simplifié] |')
print('o--------------o')
print()
difficulty = input('Conbien de chances maximal voulez vous : ')
if difficulty.isdigit() == True:
    difficulty = int(difficulty)
    
    loop = 1
    while loop <= difficulty:
        print('Question numéro : ' + str(loop))
        theinput = int(input('Entrez un nombre : '))
        if a == theinput:
            print('Vous avez gagné')
            print('Le nombre a deviner a été ' + str(a) + ' avec ' + str(loop) + ' chances !')
            break
        if theinput > a:
            print('Votre nombre est trop grand')
        elif theinput < a:
            print('Votre nombre est trop petit')
        if loop == difficulty :
            print('Vous avez perdu')
            print('Le nombre a deviner a été ' + str(a) )
        loop += 1
else:
    print('Erreur : Vous ne pouvez pas faire des phases ou des lettres dans ce champ de texte !')