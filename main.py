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
#Alban a utilisé dex expect,j'ai oublié comment ca fonctione donc je  vais copie colle.
#En plus je dois convertir plusieurs trucs en 1 trucssi j'ai bien compris et flm de faire en court comme tu avais fait Alban.

# Victor j'ai modifié qq trucs de ton programme mais il est très bien. Le problème, c'est que pour les heurs, minutes et 
# secondes, t'as mis un while True sans break donc tu peux pas sortir de la boucle : à corriger avec le système de varibale
# égale à false ou true.


        e="false"
        while e=="false":
            try:
                jrs2 = int(input("Entre un nombre de jours : "))
                if jrs2 < 0:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    e="true"
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        while True:
            try:
                hrs2 = int(input("Entre un nombre d'heures : "))
                if hrs2 < 0 or hrs2>24:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    e="false"
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        while True:
            try:
                mins2 = int(input("Entre un nombre de minutes : "))
                if mins2 < 0 or mins2>60:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    e="false"
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        while True:
            try:
                sec2 = int(input("Entre un nombre de secondes : "))
                if sec2 < 0 or sec2>60:
                    print("Entrée incorrecte")
                    time.sleep(1)
                else:
                    e="false"
            except ValueError:
                print("Entrée incorrecte")
                time.sleep(1)

        total = jrs2 * 86400 + hrs2 * 3600 + mins2 * 60 + sec2
        print(jrs2, "jour(s)", hrs2," heure(s)", mins2," minute(s) et",sec2, "seconde(s) valent ",total," secondes.")
        time.sleep(4)

    else:
        print("Au revoir !")
        #choix = 3
        
