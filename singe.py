#classe singe
#declare la classe
class Banane:

    def __init__(self, couleur):
        #attribut
        self.couleur = couleur

class Singe:

    def __init__(self, prenom):
        #attribut
        self.prenom = prenom

    # declare une methode
    def mange(self, banane):
        phrase = str(self.prenom) + ' mange une banane ' + str(banane.couleur)
        print(phrase)


pierre = Singe('Pierre')
marie = Singe('Marie')
jaune = Banane('jaune')
verte = Banane('verte')

pierre.mange(jaune)
marie.mange(verte)
pierre.mange(verte)

