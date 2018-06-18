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
    pal = False
    for i in range(0, l):
        if(text[i] == text[indexFin]):
            pal = True
        else:
            print("Le mot " + text + " n'est pas un palindromme")
            return
        indexFin = indexFin - 1
    if(pal == True):
        print("Le mot " + text + " est un palindromme")

texte = raw_input("Test du mot : ")
palindromme(texte)