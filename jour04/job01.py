class Personne:

    def __init__(self):
        self.age = 14

    def afficher_age(self):
        print(self.age)

    def modifier_age(self, age):
        self.age = age

    def bonjour(self):
        print("Hello")


class Eleve(Personne):

    def __init__(self):
        super().__init__()
    def allerEnCours(self):
        print("Je vais en cours")
    def afficheAge(self):
        print(f"j'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self):
        super().__init__()
        self.__matiere = "Maths"

    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
personne1.afficher_age()
eleve1 = Eleve()
eleve1.afficheAge()