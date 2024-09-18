import tkinter
from tkinter import *

class Login:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()
        self.titulo = Label(self.janela, text="Login")
        self.titulo["font"] = ("Arial", 30, "bold")
        self.titulo.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 30
        self.janela3.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 40
        self.janela4.pack()

        self.nomeLabel = Label(self.janela2, text="Nome:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela2)
        self.nome["width"] = 20
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.janela3, text="Senha:", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.janela4)
        self.autenticar["text"] ="Autenticar"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 14
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label (self.janela4, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "alunabruna" and senha == "123456":
          self.mensagem["text"] = "Autenticado"
        else:
          self.mensagem["text"] = "Erro na autenticação"

root = Tk()
Login(root)
root.mainloop()