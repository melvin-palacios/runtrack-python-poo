import random

class Carte:

    def __init__(self, valeur, couleur, symbole):
        self.valeur = valeur
        self.couleur = couleur
        self.symbole = symbole

    def afficher(self):
        print(f"+-----+")
        print(f"|{self.symbole}    |")
        if self.valeur == 1:
            print(f"|  A  |")
        elif self.valeur == 11:
            print(f"|  J  |")
        elif self.valeur == 12:
            print(f"|  Q  |")
        elif self.valeur == 13:
            print(f"|  K  |")
        elif self.valeur >= 10:
            print(f"| {self.valeur}  |")
        else:
            print(f"|  {self.valeur}  |")
        print(f"+-----+")

class Jeu:

    def __init__(self, cartes):
        self.cartes = cartes
        self.main = []
        self.croupier = []
        self.score = 0
        self.running = True

    def tirer(self, joueur):
        if joueur == "croupier":
            self.croupier.append(self.cartes.pop())
        else:
            self.main.append(self.cartes.pop())
        return self.cartes.pop()

    def afficher(self):
        print("Votre main :")
        for carte in self.main:
            carte.afficher()

    def afficher_croupier(self):
        print("La main du croupier :")
        for carte in self.croupier:
            carte.afficher()

    def choix(self):
        choix = input("Voulez-vous tirer une carte ? (o/n)\n ou \nComparer les mains ? (entrée)\n")
        if choix == "o":
            self.tirer("joueur")
            self.tirer("croupier")
            self.afficher()
            self.verifier()
        elif choix == "n":
            print("Vous avez choisi de ne pas tirer de carte.")
            return
        elif choix == "":
            print("Vous avez choisi de comparer les mains.")
            self.comparer()

        else:
            print("Vous n'avez pas entré une valeur valide")
            self.choix()

    def comparer(self):
        self.afficher()
        score_joueur = self.verifier()
        print(f"Votre score est de {self.score}")
        score_croupier = self.verifier_croupier()
        self.afficher_croupier()
        print(f"Le score du croupier est de {self.score}")
        if score_joueur > score_croupier and score_joueur <= 21:
            print("Vous avez gagné")
        elif score_joueur < score_croupier and score_croupier <= 21:
            print("Vous avez perdu")
        self.running = False
    def verifier(self):
        self.score = 0
        for carte in self.main:
            if carte.valeur == 1:
                self.score += 11
            elif carte.valeur >= 10:
                self.score += 10
            else:
                self.score += carte.valeur
        if self.score > 21:
            print("Vous avez perdu")
            print(f"Votre score est de {self.score}")
            self.running = False
        return self.score

    def verifier_croupier(self):
        self.score = 0
        for carte in self.croupier:
            if carte.valeur == 1:
                self.score += 11
            elif carte.valeur >= 10:
                self.score += 10
            else:
                self.score += carte.valeur
        return self.score

    def play(self):
        self.tirer("croupier")
        self.tirer("croupier")
        self.tirer("joueur")
        self.tirer("joueur")
        self.afficher()
        while self.running:
            self.choix()

cartes = []
for i in range(1, 14):
    cartes.append(Carte(i, "coeur", "♥"))
    cartes.append(Carte(i, "carreau", "♦"))
    cartes.append(Carte(i, "pique", "♠"))
    cartes.append(Carte(i, "trèfle", "♣"))

random.shuffle(cartes)

jeu = Jeu(cartes)
jeu.play()
