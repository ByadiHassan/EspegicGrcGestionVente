from produit import Produit
try:
    p=Produit(10,'Stylo',20)
    p.afficheToi()
except Exception as ex:
    print(ex)


