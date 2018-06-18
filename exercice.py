def addition(n):
    somme = 0
    for i in range(1, n+1):
        somme = somme + i
    print(somme)

addition(3)
addition(8)

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

fibo()

def testTableau(t, n):
    if(n in t):
        print("L'entier " + str(n) + " se trouve dans le tableau")
    else:
        print("L'entier " + str(n) + " ne se trouve pas dans le tableau")

tableau = [3, 5, 0, 4]
testTableau(tableau, 5)
testTableau(tableau, 6)