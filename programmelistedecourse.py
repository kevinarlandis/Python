import sys

liste_de_course = []

user_input = int(input(""" choisissez parmis les 5 options:
                   1:ajouter un élément
                  2: supprimer un élément
                  3: afficher élément de la liste
                  4:vider la liste
                  5:quitter
                  ?Votre choix: """))
if (user_input < 1 or user_input > 5):
    print("choisissez une option valide..")
    
if user_input == 1:
    liste_de_course.append(input("donnez le nom de l'élément a ajouter: "))
    
elif user_input == 2:
    item = input("donner le nom de l'élément a retirer: ")
    if item in liste_de_course:
        liste_de_course.remove(item)
    else :
        print(f"L'élément {item} n'est pas dans la liste.")

elif user_input == 3:
    if liste_de_course:
        for i, element in enumerate(liste_de_course):
            print(i, element)
    else:
        ("votre liste ne contient aucun élément.")
        
elif user_input == 4:
    liste_de_course.clear()
    print("votre liste a été vidée.")
    
elif user_input == 5:
    sys.exit()