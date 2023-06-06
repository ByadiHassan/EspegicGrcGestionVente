import tkinter as tk
class FormGestionHabit:
    def __init__(self,fenetre:tk.Tk):
        self.fenetre=fenetre
        self.fenetre.iconify()
        self.root=tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Gestion des habits")
        self.root.iconbitmap('free.ico')
        self.btnFermer=tk.Button(self.root,text="Fermer",
        command=self.fermer,bd=10,bg="orange")
        self.btnFermer.pack(side="bottom")



        self.root.mainloop()
    def fermer(self):
        self.fenetre.deiconify()
        self.root.destroy()