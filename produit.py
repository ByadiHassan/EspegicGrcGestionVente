class Produit:
    def __init__(self,id,designation,prix):
        self.setId(id)
        self.setDesignation(designation)
        self.setPrix(prix)

    def getId(self):
        return self.__id
    def setId(self,id):
        if id>0:
            self.__id=id
        else :
            ex=Exception("L'id du produit doit être strictement positif !")
            raise ex 
    def getDesignation(self):
        return self.__designation
    def setDesignation(self,designation):
        if len(designation)>0:
            self.__designation=designation
        else :
            ex=Exception("La designation  du produit ne doit pas être vide !")
            raise ex 

    def getPrix(self):
        return self.__prix

    def setPrix(self,prix):
        if prix>0:
            self.__prix=prix
        else:
            ex=Exception("Le prix doit etre strictement positif !")
    def __str__(self):
        return str(self.__id) +'\t'+ self.__designation+'\t'+str(self.__prix)

    def afficheToi(self):
        print(self)