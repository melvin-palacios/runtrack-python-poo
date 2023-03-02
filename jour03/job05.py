class Personnage:

    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def soigner(self):
        self.vie += 10
        print("Soin de", self.nom)
    def attaquer(self, cible):
        cible.vie -= 10
        print("Attaque de", self.nom, "sur", cible.nom)

    def attaque_speciale(self, cible):
        cible.vie -= 20
        print("Attaque speciale de", self.nom, "sur", cible.nom)


class Jeu:

    def __init__(self):
        self.joueurs = []
        self.set_difficulty()
    def set_difficulty(self):
        difficulty = input("Choisir une difficulté (1 : facile, 2 : moyenne, 3 : difficile) : ")
        difficulty = int(difficulty)
        if difficulty >= 1 and difficulty <= 3:
            print("Difficulté choisie: ", difficulty)
            self.apply_difficulty(difficulty)
        else:
            print("Difficulté non valide")
            self.set_difficulty()
    def apply_difficulty(self, difficulty):
        if difficulty == 1:
            self.joueurs.append(Personnage("Joueur 1", 100))
            self.joueurs.append(Personnage("Joueur 2", 100))
        elif difficulty == 2:
            self.joueurs.append(Personnage("Joueur 1", 50))
            self.joueurs.append(Personnage("Joueur 2", 50))
        elif difficulty == 3:
            self.joueurs.append(Personnage("Joueur 1", 30))
            self.joueurs.append(Personnage("Joueur 2", 30))
    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_joueurs(self):
        for joueur in self.joueurs:
            print(joueur.nom, ":", joueur.vie, "PV")

    def tour(self,joueur, cible,count):
        choix = input(f"1: Attaquer\n2: Soigner\n3: Attaque speciale (2 tours de recharge)\n")
        if int(choix) == 1:
            joueur.attaquer(cible)
        elif int(choix) == 2:
            joueur.soigner()
        elif int(choix) == 3:
            if count % 2 == 0:
                joueur.attaque_speciale(cible)
            else:
                print("Vous ne pouvez pas utiliser cette attaque")
                self.tour(joueur, cible,count)
        else:
            print("Choix non valide")
            self.tour(joueur, cible,count)
    def verifier_vie(self):
        for joueur in self.joueurs:
            if joueur.vie <= 0:
                self.joueurs.remove(joueur)
                return True
        return False
    def jouer(self):
        count = 0
        while True:
            joueur1 = self.joueurs[0]
            joueur2 = self.joueurs[1]
            self.afficher_joueurs()
            self.tour(joueur1, joueur2,count)
            count += 1
            if self.verifier_vie():
                break
            self.afficher_joueurs()
            self.tour(joueur2, joueur1,count)
            if self.verifier_vie():
                break
            count += 1

        print("Le gagnant est: ", self.joueurs[0].nom)


Jeu = Jeu()
Jeu.jouer()