## Mini projet - Convertisseur de durée - AlbanD/T, Victor

import time

print("Bonjour, je convertis des secondes en jours, heures, minutes et secondes et des jours, heures, minutes et secondes en secondes !")
time.sleep(1)
choix=0
while choix!=3:
    print("Que veux tu faire?")
    time.sleep(1)
    print("1 : Convertir des secondes en jours, heures, minutes et secondes\n2 : Convertir des jours, heures, minutes et secondes en secondes\n3 : Quitter")
    time.sleep(1)
    
    choix=input("Alors, qu'est ce que tu choisis ?")
    while choix!="1" and choix!="2" and choix!="3":
        print("Entrée incorrecte")
        time.sleep(1)
        choix=input("Alors, qu'est ce que tu choisis ?")
    choix=int(choix)

    if choix==1:
        nbint="false"
        while nbint == "false":
            try:
                sec1 = int(input("Entre un nombre de secondes à convertir : "))
                if sec1 < 0:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    nbint = "true"
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        jrs1=sec1//86400
        hrs1=sec1//3600-jrs1*24
        mins1=sec1//60-jrs1*1440-hrs1*60
        sec1_1=sec1-jrs1*86400-hrs1*3600-mins1*60
        print(sec1, "secondes vallent : ", jrs1, "jour(s) - ", hrs1, "heure(s) - ", mins1, "minute(s) - ", sec1_1, "seconde(s)")
        time.sleep(4)

    elif choix==2:
        print("Cette partie n'est pas encore faite")
        ## Partie de Victor (il faudra enlever le print au dessus)

    else:
        print("Au revoir !")
