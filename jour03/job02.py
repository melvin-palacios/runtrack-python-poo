class CompteBancaire:
    def __init__(self, nom, prenom, solde):
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = False
        self.decouvert()

    def decouvert(self):
        if self.__solde < 0:
            self.__decouvert = True
        else:
            self.__decouvert = False

    def getNom(self):
        return self.__nom

    def getDecouvert(self):
        if self.__decouvert == True:
            return "Oui"
        else:
            return "Non"

    def getPrenom(self):
        return self.__prenom

    def getSolde(self):
        return self.__solde

    def agios(self, somme):
        if self.__decouvert == True:
            agios = somme * 0.2
            somme -= agios
            print(f"le compte est à découvert, vous avez un agios de {int(agios)}")
        return somme
    def versement(self, somme):
        if self.__decouvert == True:
            self.__solde += self.agios(somme)
            self.decouvert()
        else:
            self.__solde += somme
        print(f"Versement de {somme} effectué")
    def retrait(self, somme):
        if self.__decouvert == False:
            self.__solde -= somme
            self.decouvert()
            print(f"retrait de {somme} effectué")
    def virement(self, somme, compte):
        if self.__decouvert == False:
            if compte.getDecouvert() == "Oui":
                print(f"virement de {somme} effectué au compte de {compte.getNom()} {compte.getPrenom()}")
                compte.__solde += compte.agios(somme)
                compte.decouvert()
            else:
                print(f"virement de {somme} effectué au compte de {compte.getNom()} {compte.getPrenom()}")
                compte.__solde += somme
                compte.decouvert()
            self.decouvert()
            self.__solde -= somme
    def affiche(self):
        print("\nCompte bancaire : ")
        print("Nom : ", self.__nom)
        print("Prénom : ", self.__prenom)
        print("Solde : ", self.__solde)
        print("")

    def afficher_solde(self):
        print("Solde : ", self.__solde)

compte1 = CompteBancaire("Plc", "Melvin", 2000)
compte2 = CompteBancaire("Di-do", "Max", -500)
compte1.affiche()
compte2.affiche()
compte1.virement(630, compte2)
compte1.affiche()
compte2.affiche()