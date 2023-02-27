class Produit:

    def __init__(self):
        self.nom = ""
        self.prixHT = 0
        self.TVA = 20

    def modifierNom(self, nom):
        self.nom = nom
    def modifierPrixHT(self, prixHT):
        self.prixHT = prixHT
    def calculerPrixTTc(self):
        return self.prixHT + (self.prixHT * self.TVA / 100)
    def afficherNom(self):
        return self.nom
    def afficherPrixHT(self):
        return "Prix : " + str(self.prixHT) + "€"
    def afficherTVA(self):
        return  "TVA : " + str(self.TVA)
    def listeProduit(self):
        return "Nom: " + self.nom + " PrixHT: " + str(self.prixHT) + " TVA: " + str(self.TVA)

Produit1 = Produit()
Produit1.modifierNom("Pomme")
Produit1.modifierPrixHT(1.5)
print(Produit1.afficherNom())
print(Produit1.afficherPrixHT())
print(Produit1.afficherTVA())
print(Produit1.listeProduit())