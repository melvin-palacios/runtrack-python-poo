class Livre:

    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__nbPages = 0
        self.__disponible = True

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nbPages(self, nbPages):
        if nbPages < 0 or nbPages != int(nbPages):
            print("Erreur : Le nombre de pages doit être positif et entier")
        else:
            self.__nbPages = nbPages

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nbPages(self):
        return self.__nbPages

    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False

    def emprunter(self):
        if self.verification() == True:
            self.__disponible = False
            print("Le livre a été emprunté")
        else:
            print("Le livre ne peut pas été emprunté")

    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
            print("Le livre a été rendu")
        else:
            print("Le livre ne peut pas être rendu")

livre1 = Livre()
livre1.set_titre("Cendrillon")
livre1.set_auteur("Charles Perrault")
livre1.set_nbPages(100)
livre1.emprunter()
livre1.emprunter()
livre1.rendre()
livre1.rendre()
livre1.emprunter()