class Livre:

    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__nbPages = 0

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

livre1 = Livre()
livre1.set_titre("Cendrillon")
livre1.set_auteur("Charles Perrault")
livre1.set_nbPages(100)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nbPages())
livre1.set_nbPages(-10)
livre1.set_nbPages(10.5)
print(livre1.get_nbPages())