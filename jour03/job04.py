class Joueur:
    def __init__(self, nom, numero, posotion, nombre_but, nombre_passe_d, carte_rouge, carte_jaune):
        self.nom = nom
        self.numero = numero
        self.posotion = posotion
        self.nombre_but = nombre_but
        self.nombre_passe_d = nombre_passe_d
        self.carte_rouge = carte_rouge
        self.carte_jaune = carte_jaune

    def marquer_but(self):
        self.nombre_but += 1

    def faire_passe_d(self):
        self.nombre_passe_d += 1

    def recevoir_carte_jaune(self):
        self.carte_jaune += 1

    def recevoir_carte_rouge(self):
        self.carte_rouge += 1

    def afficher_stat(self):
        print("Nom: ", self.nom)
        print("Numero: ", self.numero)
        print("Position: ", self.posotion)
        print("Nombre de but: ", self.nombre_but)
        print("Nombre de passe décisive: ", self.nombre_passe_d)
        print("Nombre de carte jaune: ", self.carte_jaune)
        print("Nombre de carte rouge: ", self.carte_rouge)

class Equipe:

    def __init__(self,name):
        self.name = name
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_joueurs(self):
        print("Equipe: ", self.name)
        print("")
        for joueur in self.joueurs:
            joueur.afficher_stat()
            print("")

    def mettreAJourStat(self, joueur, but, passe_d, carte_jaune, carte_rouge):
        joueur.nombre_but += but
        joueur.nombre_passe_d += passe_d
        joueur.carte_jaune += carte_jaune
        joueur.carte_rouge += carte_rouge



joueur1 = Joueur("Messi", 10, "attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Ronaldo", 7, "attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Neymar", 11, "attaquant", 0, 0, 0, 0)
joueur4 = Joueur("Mbappe", 9, "attaquant", 0, 0, 0, 0)
joueur5 = Joueur("Kante", 7, "milieu", 0, 0, 0, 0)
joueur6 = Joueur("Pogba", 6, "milieu", 0, 0, 0, 0)
joueur7 = Joueur("Kimpembe", 3, "defenseur", 0, 0, 0, 0)
joueur8 = Joueur("Varane", 4, "defenseur", 0, 0, 0, 0)
joueur9 = Joueur("Lloris", 1, "gardien", 0, 0, 0, 0)
joueur10 = Joueur("Navas", 1, "gardien", 0, 0, 0, 0)

equipe1 = Equipe("France")
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)
equipe1.ajouter_joueur(joueur4)
equipe1.ajouter_joueur(joueur7)
equipe1.ajouter_joueur(joueur9)

equipe2 = Equipe("France_V2")
equipe2.ajouter_joueur(joueur3)
equipe2.ajouter_joueur(joueur5)
equipe2.ajouter_joueur(joueur6)
equipe2.ajouter_joueur(joueur8)
equipe2.ajouter_joueur(joueur10)



equipe1.afficher_joueurs()
equipe2.afficher_joueurs()

equipe1.mettreAJourStat(joueur1, -10, 0, 20, 20)
equipe1.mettreAJourStat(joueur2, 999, 1, 0, 0)
equipe1.mettreAJourStat(joueur4, 0, 0, 1, 0)

equipe1.afficher_joueurs()
equipe2.afficher_joueurs()
