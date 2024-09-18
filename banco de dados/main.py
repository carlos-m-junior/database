import tkinter as tk
from tkinter import messagebox

def sair():
    root.quit()

def sobre():
    messagebox.showinfo("Sobre", "Este é um aplicativo de exemplo.")

# Criar a janela principal
root = tk.Tk()
root.title("Aplicativo Simples")

# Criar um menu
menubar = tk.Menu(root)

# Menu 'Arquivo'
arquivo_menu = tk.Menu(menubar, tearoff=0)
arquivo_menu.add_command(label="Sair", command=sair)
menubar.add_cascade(label="Arquivo", menu=arquivo_menu)

# Menu 'Ajuda'
ajuda_menu = tk.Menu(menubar, tearoff=0)
ajuda_menu.add_command(label="Sobre", command=sobre)
menubar.add_cascade(label="Ajuda", menu=ajuda_menu)

# Configurar o menu na janela
root.config(menu=menubar)

# Executar o aplicativo
root.mainloop()