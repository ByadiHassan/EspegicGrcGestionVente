from produit import Produit
from habit import Habit
class Clavier:
    @staticmethod
    def getString(msg):
        return input(msg)    
    @staticmethod
    def getInt(msg):
        while True:
            try:
                return int(Clavier.getString(msg))                
            except Exception as ex:
                print(ex)
    @staticmethod
    def getFloat(msg):
        while True:
            try:
                return float(Clavier.getString(msg))                
            except Exception as ex:
                print(ex)
    @staticmethod
    def getProduit():
       # id=Clavier.getInt("Tapez l'id du produit ? ")
        design=Clavier.getString("Tapez la désignation du produit ? ")
        prix= Clavier.getFloat("Tapez le prix du produit ? ")
        pr=Produit(design,prix)
        return pr
        #return Produit(Clavier.getInt("Tapez l'id du produit ? "),
        # Clavier.getString("Tapez la désignation du produit ? "),
        # Clavier.getFloat("Tapez le prix du produit ? "))
    @staticmethod
    def getHabit():       
        return Habit(Clavier.getString("Tapez la désignation du produit ? "),
        Clavier.getFloat("Tapez le prix du produit ? "),
        Clavier.getString("Tapez la couleur du produit ? "),
        Clavier.getString("Tapez la Taille du produit ? "))