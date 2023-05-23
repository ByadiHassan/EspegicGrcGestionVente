from magasin import Magasin
from produit import Produit
from clavier import Clavier
from os import system
mag=Magasin()
choix=0
while choix!=6:
    system("cls")
    choix=Clavier.getInt("1. Ajouter\n2. Afficher\n3. Enregistrer\n4. Ouvrir\n5. Chercher\n6. Quitter\nTapez votre choix : ")
    if choix==1:
        mag.ajouter(Clavier.getProduit())
        # id=int(input("Tapez l'id du produit ? "))
        # desig=input("Tapez la désignation  du produit ? ")
        # prix= float(input("Tapez le prix du produit ? "))
        # pr=Produit(id,desig,prix)
        # mag.ajouter(pr)
    elif choix==2:
        mag.afficher()
        system("pause")
    elif choix==3:
        mag.enregistrer()
    elif choix==4:
        mag.charger()
        mag.afficher()
        
        system("pause")
    elif choix==5:
        #id=int(input("Tapez l'id du produit à chercher  ? "))
        id:int=Clavier.getInt("Tapez l'id du produit à chercher  ? ")
        if mag.exists(id) :
            pr:Produit=mag.chercher(id)
            pr.afficheToi()            
        else:
            print("Aucun produit de la liste ne possède cet Id !!!")
        system("pause")
