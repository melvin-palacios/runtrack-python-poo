class Personnage:

    def __init__(self):
        self.x = 0
        self.y = 5
    def gauche(self):
        self.x -= 1
    def droite(self):
        self.x += 1
    def haut(self):
        self.y += 1
    def bas(self):
        self.y -= 1

    def position(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

Personnage1 = Personnage()
print(Personnage1.position())
Personnage1.gauche()
Personnage1.bas()
print(Personnage1.position())
Personnage1.droite()
Personnage1.haut()
print(Personnage1.position())