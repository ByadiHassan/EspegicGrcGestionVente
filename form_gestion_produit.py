import tkinter as tk
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

        self.btnAjouter=tk.Button(self.frameButton,text="Ajouter",
        bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",
        command=self.ajouter
       )

        self.btnAjouter.pack(side="left")

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
    def fermer(self):
        self.fenetre.deiconify()
        self.root.destroy()
    def ajouter(self):
        try:
            self.mag.ajouter(Produit(int(self.entryId.get()),self.entryDesign.get(),float(self.entryPrix.get())))
        except Exception as ex:
            messagebox.showinfo(title="Alerte",message=ex)   
    def afficher(self):
        self.fenetre.deiconify()
        self.root.destroy()
    def enregistrer(self):
        self.fenetre.deiconify()
        self.root.destroy()
    def ouvrir(self):
        self.fenetre.deiconify()
        self.root.destroy()
    def chercher(self):
        self.fenetre.deiconify()
        self.root.destroy()