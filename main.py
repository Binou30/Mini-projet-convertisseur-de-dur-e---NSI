## Mini projet - Convertisseur de durée - AlbanD/T, Victor
##
import time
##
## Partie informations
##
print("Bonjour, je convertis des secondes en jours, heures, minutes et secondes et des jours, heures, minutes et secondes en secondes !")
time.sleep(1)
print("Que veux tu faire?")
time.sleep(1)
print("1 : Convertir des secondes en jours, heures, minutes et secondes\n2 : Convertir des jours, heures, minutes et secondes en secondes\n3 : Quitter")
time.sleep(3)
##
## Partie conversion et choix
##
choix = input("Alors, qu'est ce que tu choisis ?")
while choix != "1" and choix != "2" and choix != "3":
    print("Entrée incorrecte")
    time.sleep(1)
    choix = input("Alors, qu'est ce que tu choisis ?")
choix = int(choix)

if choix == 1:
    ## Partie de Alban T (à compléter par Alban)
    print("Cette partie n'est pas encore faite")
elif choix == 2:
    ## Partie de Victor : convertir une durée en secondes
    jours = int(input("Combien de jours ? "))
    heures = int(input("Combien d'heures ? "))
    minutes = int(input("Combien de minutes ? "))
    secondes = int(input("Combien de secondes ? "))

    total_secondes = jours * 24 * 60 * 60
    total_secondes += heures * 60 * 60
    total_secondes += minutes * 60
    total_secondes += secondes

    print("La durée correspond à", total_secondes, "secondes.")

print("Au revoir !")
