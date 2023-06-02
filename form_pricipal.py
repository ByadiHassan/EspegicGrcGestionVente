import tkinter as tk
from form_gestion_produit import FormGestionProduit
from form_gestion_habit import FormGestionHabit
class FormPrincipal:
    def __init__(self):
        self.root=tk.Tk()  
        self.root.iconbitmap("bing.ico" )
        self.root.geometry("750x500")
        self.root.title(" Form Principal")
        self.lblPrompt=tk.Label(self.root,text="Bienvenu à l'application gestion des clients",bg="Blue",fg="White",font="Arial 16 italic bold")
        self.lblPrompt.pack(side="top")
        self.btnQuitter=tk.Button(self.root,text="Quitter",command=self.root.destroy,bd=10,bg="Red")
        self.btnQuitter.pack(side="bottom")
        self.frameButton=tk.Frame(self.root) 
        self.frameButton.pack(expand='YES')  
        self.btnGestionProduit=tk.Button(self.frameButton,text="Gestion des Produits",bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",command=self.openFormGestionProduit)
        self.btnGestionProduit.pack(side="left")
        self.btnGestionHabit=tk.Button(self.frameButton,text="Gestion des Habits",bd=10,bg="Blue",fg="White",font="Arial 16 italic bold",command=self.openFormGestionHabit)
        self.btnGestionHabit.pack(side="left")
        self.btnGestionProduitE=tk.Button(self.frameButton,text="Gestion Produit Elect.",bd=10,bg="Blue",fg="White",font="Arial 16 italic bold")
        self.btnGestionProduitE.pack(side="left")
        
        


        self.root.mainloop()
   
    def openFormGestionProduit(self):
        FormGestionProduit()

    def openFormGestionHabit(self):
        FormGestionHabit()

        