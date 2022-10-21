import random

f = open("/home/bendris/python-project/dico_france.txt",encoding="ISO-8859-1")
a = f.read()
b = a.split()

c = random.choice(b)
print(c)

for i in c:
    print("_", end = " ")
    end = -1

solution = "casserole"

nbtenta = input("choisis ton niveau de difficulté (expert, intermédiaire, débutant)")

tentatives = ""

if nbtenta == "expert":
    tentatives = 4
if nbtenta =="intermédiaire":          #demande du niveau souhaiter + nbr de vie 
    tentatives = 7                         
if nbtenta == "débutant":
    tentatives = 10


    print(tentatives)

    affichage = ""
    for l in solution:
        affichage = affichage + "_ "          #lettre pas encore découverte + maj de l'affichage

    lettres_trouvees = ""  


    print("mot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")        #demande user sa proposition de lettre


        
    if proposition in solution :
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bien vu!")                                 #indiquer si la lettre apartient ou pas
    else:
        tentatives = tentatives -1
        print("-> Nope. Il vous reste", tentatives, "tentatives")




    while tentatives>0:
        print("Mot à deviner : ", affichage)
        proposition = input("proposer une lettre: ")
        if proposition in solution:
            lettres_trouvees = lettres_trouvees + proposition
            print("-> Bien vu!")
        else:                                          #boucle pour répeter les instruction precèdente
            tentatives = tentatives - 1                #instructions répétées tant que le nombre de tentatives n'est pas dépassé
            print("-> Nope. Il vous reste", tentatives, "tentatives")


        affichage = ""
        for x in solution:
            if x in lettres_trouvees:
                affichage += x + " "                       #affichage de chauque lettre de la solution
            else:
                affichage += "_ "



            if "_" not in affichage:
                print(">>> Gagné! <<<")
                break

        

print("    * Fin de la partie *    ")



