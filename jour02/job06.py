class Commande:

    def __init__(self, num_commande, liste_produits):
        self.__num_commande = num_commande
        self.__liste_produits = liste_produits
        self.__statut = "En cours"
        self.__commande = []
    def get_num_commande(self):
        return self.__num_commande

    def get_liste_produits(self):
        return self.__liste_produits

    def get_statut(self):
        return self.__statut

    def get_commande(self):
        return self.__commande

    def set_statut(self, statut):
        self.__statut = statut

    def add_produit(self, produit):
        self.__commande.append(produit)
        print(f"{produit} ajouté")
    def annuler_commande(self):
        self.__statut = "Annulée"
        self.__liste_produits = []
        print("Commande annulée")

    def prix_commande(self):
        prix = 0
        for produit in self.__commande:
            prix += self.__liste_produits[produit]
        return prix

    def prix_commande_TTC(self):
        return self.prix_commande() * 1.2
    def afficher_commande(self):
        print("Commande n°", self.__num_commande, ":", self.__commande, "Prix :", self.prix_commande_TTC(), "€")
    def paiement_commande(self):
        self.__statut = "Payée"
        print("Commande payée")

plat = {
    "Pomme": 1,
    "Poire": 1.5,
    "Banane": 1.2,
    "Orange": 1.8
}
commande1 = Commande(1, plat)
print(commande1.get_statut())
print('----------------')
print("liste des produits :")
print(commande1.get_liste_produits())
print('----------------')
commande1.add_produit("Pomme")
commande1.add_produit("Banane")
commande1.add_produit("Orange")
print('----------------')
commande1.afficher_commande()
commande1.paiement_commande()