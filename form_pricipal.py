import tkinter as tk
class FormPrincipal:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.title(" Form Principal")
        self.lblPrompt=tk.Label(self.root,text="Bonjour tout le monde",bg="Blue",fg="White",font="Arial 16 bold")
        self.lblPrompt.pack(side="top")
        self.btnQuitter=tk.Button(self.root,text="Quitter",command=self.root.destroy,bd=10,bg="Red")
        self.btnQuitter.pack(side="bottom")

        self.root.mainloop()
