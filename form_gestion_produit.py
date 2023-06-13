import tkinter as tk
from tkinter import tix
from tkinter import messagebox
from magasin import Magasin
from produit import Produit
class FormGestionProduit:
    def __init__(self,fenetre:tk.Tk):
        self.mag=Magasin()
        self.fenetre=fenetre
        self.fenetre.iconify()
        self.root=tk.Tk()
        self.root.geometry("1080x700")
        self.root.title("Gestion des produits")
        self.root.iconbitmap('free.ico')
        self.frameEntry=tk.LabelFrame(self.root,text="Entry",bg="yellow")
        self.frameEntry.pack(expand=1)

        self.lblId=tk.Label(self.frameEntry,text="Id", 
        font="Arial 16 italic bold",bg="yellow")

        self.lblId.grid(column=0,row=0,sticky=tk.W)
        self.entryId=tk.Entry(self.frameEntry, 
        font="Arial 16 italic bold")
        self.entryId.grid(column=1,row=0)

        self.lblDesign=tk.Label(self.frameEntry,text="Designation", 
        font="Arial 16 italic bold",bg="yellow")
        self.lblDesign.grid(column=0,row=1,sticky=tk.W)
        self.entryDesign=tk.Entry(self.frameEntry, 
        font="Arial 16 italic bold")
        self.entryDesign.grid(column=1,row=1)

        self.lblPrix=tk.Label(self.frameEntry,text="Prix",
        font="Arial 16 italic bold",bg="yellow")
        self.lblPrix.grid(column=0,row=2,sticky=tk.W)
        self.entryPrix=tk.Entry(self.frameEntry,
        font="Arial 16 italic bold")
        self.entryPrix.grid(column=1,row=2)

        self.frameButton=tk.Frame(self.root) 
        self.frameButton.pack(expand='YES') 

        self.frameRecherche=tk.LabelFrame(self.root,text='Recherche')
        
        self.lblRechercheId=tk.Label(self.frameRecherche, text="Id",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold")
        self.lblRechercheId.grid(row=0,column=0,sticky=tk.W)

        self.entryRechercheId=tk.Entry(self.frameRecherche,
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold")
        self.entryRechercheId.grid(row=0,column=1)

        self.btnOkRecherche=tk.Button(self.frameRecherche,command=self.lancerRecherche, text="Ok",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold")
        self.btnOkRecherche.grid(row=1,column=0)

        self.btnAnnulerRecherche=tk.Button(self.frameRecherche,command=self.annulerRecherche, text="Annuler",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold")
        self.btnAnnulerRecherche.grid(row=1,column=1)
        

        self.btnAjouter=tk.Button(self.frameButton,text="Ajouter",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",
        command=self.ajouter)
        self.btnAjouter.pack(side="left")

        self.btnAfficher=tk.Button(self.frameButton,text="Afficher",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",
        command=self.afficher)
        self.btnAfficher.pack(side="left")

        self.btnEnregistrer=tk.Button(self.frameButton,text="Enregistrer",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",
        command=self.enregistrer
        )

        self.btnEnregistrer.pack(side="left")

        self.btnOuvrir=tk.Button(self.frameButton,text="Ouvrir",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold"
        ,command=self.ouvrir)
        self.btnOuvrir.pack(side="left")

        self.btnChercher=tk.Button(self.frameButton,text="Chercher",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",command=self.chercher)
        self.btnChercher.pack(side="left")

        self.btnFermer=tk.Button(self.root,text="Fermer",
        command=self.fermer,bd=10,bg="orange")
        self.btnFermer.pack(side="bottom")

        self.root.mainloop()




    def lancerRecherche(self):
        if self.mag.exists(int(self.entryRechercheId.get())):
            pr:Produit=self.mag.chercher(int(self.entryRechercheId.get()))
            self.effacer()
            self.entryId.insert(0,pr.getId())
            self.entryDesign.insert(0,pr.getDesignation())
            self.entryPrix.insert(0,pr.getPrix())
        else:
            messagebox.showwarning(title="Recherche",message="Ce produit n'existe pas !")


        self.frameRecherche.pack_forget()
    def annulerRecherche(self):
        self.frameRecherche.pack_forget()
    def fermer(self):
        self.fenetre.deiconify()
        self.root.destroy()

    def ajouter(self):
        try:
            self.mag.ajouter(Produit(int(self.entryId.get()),self.entryDesign.get(),float(self.entryPrix.get())))
            self.effacer()
            self.entryId.focus()
        except Exception as ex:
            messagebox.showinfo(title="Alerte",message=ex)   
   
    def afficher(self):
        fen=tix.Tk()
        fen.title("Liste des produits")
        fen.geometry("380x300")
        sw=tix.ScrolledWindow(fen)
        sw.pack(fill=tk.BOTH,expand=1)
        i=0
        
        for item in self.mag.getProduits():
            e1 = tix.Entry(sw.window, width=10, fg='blue',font=('Arial',16,'bold')) 
            e1.grid(row=i, column=0) 
            e1.insert(0, item.getId())

            self.e2 = tix.Entry(sw.window, width=10, fg='blue',font=('Arial',16,'bold')) 
            self.e2.grid(row=i, column=1) 
            self.e2.insert(0, item.getDesignation())
            
            self.e3 = tix.Entry(sw.window, width=10, fg='blue',font=('Arial',16,'bold')) 
            self.e3.grid(row=i, column=2) 
            self.e3.insert(tix.END, item.getPrix())
            i+=1
        fen.mainloop()



        
    def enregistrer(self):
        self.mag.enregistrer()
    def ouvrir(self):
        self.mag.charger()
    def chercher(self):
        self.frameRecherche.pack(expand=1)

    def effacer(self):
        self.entryId.delete(0,len(self.entryId.get()))
        self.entryDesign.delete(0,len(self.entryDesign.get()))
        self.entryPrix.delete(0,len(self.entryPrix.get()))