## Mini projet - Convertisseur de durée - AlbanD/T, Victor
##
import time
##
print("Bonjour, je convertis des secondes en jours, heures, minutes et secondes et des jours, heures, minutes et secondes en secondes !")
time.sleep(1)
print("Que veux tu faire?")
time.sleep(1)
print("1 : Convertir des secondes en jours, heures, minutes et secondes\n2 : Convertir des jours, heures, minutes et secondes en secondes\n3 : Quitter")
time.sleep(3)
##
choix=input("Alors, qu'est ce que tu choisis ?")
while choix!="1" and choix!="2" and choix!="3":
    print("Entrée incorrecte")
    time.sleep(1)
    choix=input("Alors, qu'est ce que tu choisis ?")
choix=int(choix)
if choix==1:
    nbint="false"
    while nbint=="false":
        try:
            sec1=int(input("Entre un nombre de secondes à convertir"))
            nbint="true"
        except ValueError:
            print("Entrée incorrecte")
            time.sleep(1)
    print("Cette partie n'est pas encore faite")
else:
    print("Cette partie n'est pas encore faite")
    ## Partie de Victor (il faudra enlever le print en dessous)
print("Au revoir !")