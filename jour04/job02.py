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

eleve1 = Eleve()
eleve1.modifier_age(15)
eleve1.afficheAge()
eleve1.bonjour()
eleve1.allerEnCours()

prof1 = Professeur()
prof1.modifier_age(40)
prof1.afficher_age()
prof1.bonjour()
prof1.enseigner()