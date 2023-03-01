class Ville:

    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population
        print(f"Création de la ville de {self.__nom} avec une population de {self.__population} habitants")
    def get_nom(self):
        return self.__nom

    def get_population(self):
        return self.__population

    def set_population(self, population):
        self.__population += population

class Personne:

    def __init__(self, prenom, age, ville):
        self.__prenom = prenom
        self.__age = age
        self.__ville = ville
        print(f"Création de la personne {self.__prenom} de {self.__age} ans habitant à {self.__ville.get_nom()}")
        self.ajouter_population()

    def get_prenom(self):
        return self.__prenom

    def get_ville(self):
        return self.__ville

    def get_age(self):
        return self.__age
    def set_ville(self, ville):
        self.__ville = ville

    def ajouter_population(self):
        self.__ville.set_population(1)
        print(f"1 personne ajouté à la population de {self.__ville.get_nom()}")



paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)
personne1 = Personne("John", 45, paris)
personne2 = Personne("Myrtille", 4, paris)
personne3 = Personne("Chloé", 18, marseille)
print(paris.get_population())
print(marseille.get_population())
