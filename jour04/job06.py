class Vehicule:

    def __init__(self, marque, annee, prix ,modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def informationVehicule(self):
        print("Marque: ", self.marque)
        print("Modèle: ", self.modele)
        print("Année: ", self.annee)
        print("Prix: ", self.prix)


class Voiture(Vehicule):

    def __init__(self, marque, annee, prix, modele):
        super().__init__(marque, annee, prix, modele)
        self.porte = 4

    def informationVehicule(self):
        super().informationVehicule()
        print("Portes: ", self.porte)

class Moto(Vehicule):

    def __init__(self,marque, annee, prix, modele):
        super().__init__(marque, annee, prix, modele)
        self.roue = 2

    def informationVehicule(self):
        super().informationVehicule()
        print("Nombre de roue :", self.roue)

voiture1 = Voiture("Toyota", 2018, 20000, "Corolla")
voiture1.informationVehicule()

moto1 = Moto("Honda", 2015, 5000, "CBR")
moto1.informationVehicule()