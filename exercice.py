import random

def addition(n):
    somme = 0
    for i in range(1, n+1):
        somme = somme + i
    print(somme)

#addition(3)
#addition(8)

########################################################

def fibo():
    n2 = 0
    n1 = 1
    suite = [0]
    for i in range(1, 20):
        somme = n1 + n2
        n2 = n1
        n1 = somme
        suite.append(somme)

    print(suite)

#fibo()

########################################################

def testTableau(t, n):
    if(n in t):
        print("L'entier " + str(n) + " se trouve dans le tableau")
    else:
        print("L'entier " + str(n) + " ne se trouve pas dans le tableau")

tableau = [3, 5, 0, 4]
#testTableau(tableau, 5)
#testTableau(tableau, 6)

#########################################################

def inArray(table, var):
    for i in table:
        if(i == var):
            print("L'entier " + str(var) + " se trouve dans le tableau")
            return
        print("L'entier " + str(var) + " ne se trouve pas dans le tableau")

#inArray(tableau, 5)
#inArray(tableau, 6)

##########################################################

def indexTab(tab, var):
    l = len(tab)
    for i in range(0, l):
        if(var == tab[i]):
            print("L'entier " + str(var) + " se trouve dans le tableau a la position " + str(i))

T = [3,5,0,4,4,7]

#indexTab(T, 4)

###########################################################

def returnIndex(array, var):
    k = 0
    indice = list()
    for i in array:
        if i == var:
            indice.append(k)
        k = k + 1
    print("L'entier se trouve a la position " + str(indice))

#returnIndex(T, 4)

#######################################################

def palindromme(text):
    l = len(text)
    indexFin = l-1

    for i in range(0, l):
        if(text[i] != text[indexFin]):
            print("Le mot " + text + " n'est pas un palindromme")
            return
        indexFin = indexFin - 1

    print("Le mot " + text + " est un palindromme")

#texte = raw_input("Test du mot : ")
#palindromme(texte)

#####################################################

def nbPrem(n):
    for i in range(2,n-1):
        if n % i == 0:
            # print(str(n) + " divisible par " + str(i))
            return False
    return True

def listNb():
    for n in range(2,99):
        if nbPrem(n) == True:
            print("Nombre premier " + str(n))

#listNb()

#################################################

def comparateur():
    max = 0;
    for i in range(0,10):
        chiffre = raw_input("Entrez un chiffre : ")
        if(int(chiffre) > max):
            max = int(chiffre)
    print("Le plus grand chiffre que vous avez entre est " + str(max))

#comparateur()

################################################

def montyHall():
    nbSimul = 1000
    sommeTestChange = 0
    sommeTestChangeGagne = 0
    sommeTestGarde = 0
    sommeTestGardeGagne = 0
    pourcentChange = 0
    pourcentGarde = 0
    for i in range(0, nbSimul):
        #portes, pactol et choix1 cree
        portes = [1, 2, 3]
        gagne = random.choice(portes)
        choix1 = random.choice(portes)

        #porte sans cadeau : on remove le pactol (gagne)
        porteRestanteVide = [1, 2, 3]
        porteRestanteVide.remove(gagne)

        #si le joueur a choisi la porte gagnante, on supprime le choix1 des portes vides
        if(gagne != choix1):
            porteRestanteVide.remove(choix1)

        #on choisit parmi les portes vides la porte a ouvrir et on l'enleve des portes
        porteOuverte = random.choice(porteRestanteVide)
        portes.remove(porteOuverte)

        #parmi les portes restantes, on fait un choix2
        choix2 = random.choice(portes)

        #si le choix2 = choix1, on calcule le pourcentage de gain
        if(choix2 == choix1):
            sommeTestGarde = sommeTestGarde + 1
            if(choix2 == gagne):
                sommeTestGardeGagne = sommeTestGardeGagne + 1

            pourcentGarde = sommeTestGardeGagne * 100 / sommeTestGarde

        # si le choix2 != choix1, on calcule le pourcentage de gain
        if (choix2 != choix1):
            sommeTestChange = sommeTestChange + 1
            if (choix2 == gagne):
                sommeTestChangeGagne = sommeTestChangeGagne + 1

            pourcentChange = sommeTestChangeGagne * 100 / sommeTestChange


        if(nbSimul < 10):
            print("Le pactol se trouve ici : " + str(gagne))
            print("Le choix 1 est : " + str(choix1))
            print("Les portes restantes sont : " + str(porteRestanteVide))
            print("La porte ouverte est : " + str(porteOuverte))

    print("Le taux de reussite en changeant de porte est de " + str(pourcentChange) + "%")
    print("Le taux de reussite en gardant la porte est de " + str(pourcentGarde) + "%")

#montyHall()



