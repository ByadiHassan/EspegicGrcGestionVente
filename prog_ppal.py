from magasin import Magasin
from produit import Produit
mag=Magasin()
p1=Produit(10,'Ecran',1000)
p2=Produit(11,'Clavier',250)
mag.ajouter(p1)
mag.ajouter(p2)
mag.afficher()



