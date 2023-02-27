class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):
        return self.rayon * self.rayon * 3.14
    def diametre(self):
        return self.rayon * 2
    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        print("Rayon : " + str(self.rayon))
        print("Aire : " + str(self.aire()))
        print("Diametre : " + str(self.diametre()))

print("Cercle 1")
Cercle1 = Cercle(5)
Cercle1.afficherInfos()
print("\nCercle 2")
Cercle2 = Cercle(10)
Cercle2.afficherInfos()