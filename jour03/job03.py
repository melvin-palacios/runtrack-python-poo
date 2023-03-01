class Tache:
    def __init__(self, titre, description):
        self.statut = "En cours"
        self.titre = titre
        self.description = description

class ListeDeTache:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
    def afficherListe(self):
        for tache in self.taches:
            print(f"Categorie: {tache.titre} \nDescription: {tache.description} \nStatus: {tache.statut}\n\n")

    def suprimerTache(self, tache):
        self.taches.remove(tache)

    def marqueCommeFinie(self, tache):
        tache.statut = "Finie"

    def filtrerListe(self, statut):
        print(f"Liste des taches {statut}:\n")
        for tache in self.taches:
            if tache.statut == statut:
                print(f"Categorie: {tache.titre} \nDescription: {tache.description} \nStatus: {tache.statut}\n")

tache1 = Tache("Faire les courses", "Acheter du pain")
tache2 = Tache("Faire les courses", "Acheter du lait")
tache3 = Tache("Faire les courses", "Acheter du beurre")
tache4 = Tache("Faire les courses", "Acheter du chocolat")

liste = ListeDeTache()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)
liste.afficherListe()

liste.marqueCommeFinie(tache2)
liste.marqueCommeFinie(tache4)

liste.filtrerListe("Finie")
