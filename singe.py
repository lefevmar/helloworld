#classe singe
#declare la classe
class Banane:

    def __init__(self, couleur):
        #attribut
        self.couleur = couleur
        print("Creation d'une banane " + self.couleur)

class Singe:

    def __init__(self, prenom):
        #attribut
        self.prenom = prenom
        print('Creation du singe ' + self.prenom)

    # declare une methode
    def mange(self, banane):
        phrase = str(self.prenom) + ' mange une banane ' + str(banane.couleur)
        print(phrase)

    def reproduire(self, singe, nomEnfant):
        print(str(self.prenom) + ' se reproduit avec ' + str(singe.prenom) + ' pour faire ' + nomEnfant)
        enfant = Singe(nomEnfant)
        return enfant



pierre = Singe('Pierre')
marie = Singe('Marie')
jaune = Banane('jaune')
verte = Banane('verte')
bleue = Banane('bleue')

pierre.mange(jaune)
marie.mange(verte)
pierre.mange(verte)
marie.mange(bleue)

pierre.reproduire(marie, 'Eliott')
