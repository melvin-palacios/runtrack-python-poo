class Voiture:

    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__reservoir = 50
        self.__en_marche = False

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def verifier_reservoir(self):
        if self.__reservoir > 5:
            print("Le réservoir contient " + str(self.__reservoir) + " litres")
            return True
        else:
            return False

    def demarrer(self):
        if self.verifier_reservoir():
            self.__en_marche = True
            print("La voiture démarre")
        else:
            print("Le réservoir est vide")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête")

voiture1 = Voiture("Peugeot", "308", 2018, 0)
voiture1.demarrer()
voiture1.arreter()