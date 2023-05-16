from produit import Produit
class Magasin:
    def __init__(self):
        self.__produits=list()
    def getProduits(self):
        return self.__produits
    def setProduit(self,produits):
        self.__produits=produits

    def ajouter(self,produit):
        self.__produits.append(produit)

    def supprimer(self,produit):
        self.__produits.remove(produit)
    def afficher(self):
        for produit in self.__produits:
            produit.afficheToi()

