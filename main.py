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
        nbint=False
        while nbint==nbint==False:
            try:
                sec1 = int(input("Entre un nombre de secondes à convertir : "))
                if sec1 < 0:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    nbint = True
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
        nbint=False
        while nbint==False:
            try:
                jrs2 = int(input("Entre un nombre de jours : "))
                if jrs2 < 0:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    nbint=True
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        nbint=False
        while nbint==False:
            try:
                hrs2 = int(input("Entre un nombre d'heures : "))
                if hrs2 < 0 or hrs2>24:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    nbint=True
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        nbint=False
        while nbint==False:
            try:
                mins2 = int(input("Entre un nombre de minutes : "))
                if mins2 < 0 or mins2>60:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    nbint=True
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        nbint=False
        while nbint==False:
            try:
                sec2 = int(input("Entre un nombre de secondes : "))
                if sec2 < 0 or sec2>60:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    nbint=True
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        total = jrs2 * 86400 + hrs2 * 3600 + mins2 * 60 + sec2
        print(jrs2, "jour(s)", hrs2," heure(s)", mins2," minute(s) et",sec2, "seconde(s) valent ",total," secondes.")
        time.sleep(4)

    else:
        print("Au revoir !")
        #choix = 3
        
