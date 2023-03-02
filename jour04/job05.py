class Forme:

    def __init__(self):
        pass

    def aire(self):
        return 0

class Rectangle(Forme):

    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

class Cercle(Forme):
        def __init__(self, rayon):
            super().__init__()
            self.rayon = rayon

        def aire(self):
            return 3.14 * self.rayon ** 2



rect = Rectangle(10, 5)
print(rect.aire())

cercle = Cercle(5)
print(cercle.aire())