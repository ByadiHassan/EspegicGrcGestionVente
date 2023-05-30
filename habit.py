from produit import Produit
class Habit(Produit):
    def __init__(self,designation,prix,couleur,taille):
            super().__init__(designation,prix)
            self.setCouleur(couleur)
            self.setTaille(taille)

    def getCouleur(self):
        return self.__couleur
    def setCouleur(self,couleur):
        if len(couleur)>0:
            self.__couleur=couleur
    def getTaille(self):
        return self.__taille
    def setTaille(self,taille):
        if len(taille)>0:
            self.__taille=taille
    def __str__(self):
         return super().__str__() +'\t'+ self.__couleur+'\t'+self.__taille

