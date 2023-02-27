class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePrensenter(self):
        return "Bonjour je m'appelle " + self.prenom + " " + self.nom

Personne1 = Personne("Doe", "John")
print(Personne1.SePrensenter())

Personne2 = Personne("Dupond", "Jean")
print(Personne2.SePrensenter())

