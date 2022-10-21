
import random

f = open("/home/bendris/python-project/dico_france.txt",encoding="ISO-8859-1")
a = f.read()
b = a.split()

solution = random.choice(b)

print(solution)


#solution = random.choice(choix)

a = input("Choisis ton niveau de difficulté (débutant, intermédiaire, expert) ")

if a == "débutant" :
    tentatives = 10
if a == "intermédiaire" :
    tentatives = 7
if a == "expert" :
    tentatives = 4
#tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print("-> Nope\n")
    if a == "expert" :
        if tentatives==0:
            print(" ==========Y= ")
        if tentatives<=1:
            print(" ||/       |  ")
        if tentatives<=2:
            print(" ||        0  ")
        if tentatives<=3:
            print(" ||       /|\ ")
        if tentatives<=4:      
            print("/||           ")
            print("==============\n")
    if a == "intermédiaire":
        if tentatives==0:
            print(" ==========Y= ")
        if tentatives<=1:
            print(" ||/       |  ")
        if tentatives<=2:
            print(" ||        0  ")
        if tentatives<=3:
            print(" ||       /|\ ")
        if tentatives<=4:
            print(" ||       /|  ")       
        if tentatives<=5:
            print(" ||           ")    
        if tentatives<=6:
            print(" ||           ")    
        if tentatives<=7:
            print("/||           ")
            print("==============\n")
    if a == "débutant":
     if tentatives==0:
            print(" ==========Y= ")
    if tentatives<=1:
            print(" ||/       |  ")
    if tentatives<=2:
            print(" ||        0  ")
    if tentatives<=3:
            print(" ||       /|\ ")
    if tentatives<=4:
            print(" ||       /|  ")       
    if tentatives<=5:
            print(" ||           ")        
    if tentatives<=6:
            print(" ||           ")        
    if tentatives<=7:
            print(" ||           ")        
    if tentatives<=8:
            print(" ||           ")        
    if tentatives<=9:
            print(" ||           ")        
    if tentatives<=10:
            print("/||           ")
            print("==============\n")   
  
  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")