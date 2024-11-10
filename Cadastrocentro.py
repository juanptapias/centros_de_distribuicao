import tkinter as tk
from tkinter import messagebox

class Caminhao:
    def __init__(self, id, nome, capacidade):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade

class Entrega:
    def __init__(self, id, destinatario, endereco):
        self.id = id
        self.destinatario = destinatario
        self.endereco = endereco

class CentroDistribuicao:
    def __init__(self, id, nome, cidade, uf):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.uf = uf
        self.caminhoes = []
        self.entregas = []

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.append(caminhao)

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Centros de Distribuição")

        self.centro = CentroDistribuicao(id=1, nome="", cidade="", uf="")

        self.frame_centro = tk.Frame(self.root)
        self.frame_centro.pack(pady=10)

        tk.Label(self.frame_centro, text="Nome:").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame_centro)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(self.frame_centro, text="Cidade:").grid(row=1, column=0)
        self.entry_cidade = tk.Entry(self.frame_centro)
        self.entry_cidade.grid(row=1, column=1)

        tk.Label(self.frame_centro, text="UF:").grid(row=2, column=0)
        self.entry_uf = tk.Entry(self.frame_centro)
        self.entry_uf.grid(row=2, column=1)

        tk.Button(self.frame_centro, text="Cadastrar Centro", command=self.cadastrar_centro).grid(row=3, columnspan=2)

        self.frame_caminhao = tk.Frame(self.root)
        self.frame_caminhao.pack(pady=10)

        tk.Label(self.frame_caminhao, text="Nome do Caminhão:").grid(row=0, column=0)
        self.entry_nome_caminhao = tk.Entry(self.frame_caminhao)
        self.entry_nome_caminhao.grid(row=0, column=1)

        tk.Label(self.frame_caminhao, text="Capacidade:").grid(row=1, column=0)
        self.entry_capacidade = tk.Entry(self.frame_caminhao)
        self.entry_capacidade.grid(row=1, column=1)

        tk.Button(self.frame_caminhao, text="Adicionar Caminhão", command=self.adicionar_caminhao).grid(row=2, columnspan=2)

        self.frame_entrega = tk.Frame(self.root)
        self.frame_entrega.pack(pady=10)

        tk.Label(self.frame_entrega, text="Destinatário:").grid(row=0, column=0)
        self.entry_destinatario = tk.Entry(self.frame_entrega)
        self.entry_destinatario.grid(row=0, column=1)

        tk.Label(self.frame_entrega, text="Endereço:").grid(row=1, column=0)
        self.entry_endereco = tk.Entry(self.frame_entrega)
        self.entry_endereco.grid(row=1, column=1)

        tk.Button(self.frame_entrega, text="Adicionar Entrega", command=self.adicionar_entrega).grid(row=2, columnspan=2)

    def cadastrar_centro(self):
        nome = self.entry_nome.get()
        cidade = self.entry_cidade.get()
        uf = self.entry_uf.get()
        
        if not nome or not cidade or not uf:
            messagebox.showerror("Erro", "Nome, Cidade e UF são obrigatórios.")
            return
        
        self.centro.nome = nome
        self.centro.cidade = cidade
        self.centro.uf = uf
        
        messagebox.showinfo("Sucesso", "Centro de Distribuição cadastrado com sucesso!")

    def adicionar_caminhao(self):
        nome_caminhao = self.entry_nome_caminhao.get()
        capacidade = self.entry_capacidade.get()
        
        if not nome_caminhao or not capacidade:
            messagebox.showerror("Erro", "Nome do Caminhão e Capacidade são obrigatórios.")
            return
        
        try:
            capacidade = int(capacidade)
            caminhao = Caminhao(id=len(self.centro.caminhoes) + 1, nome=nome_caminhao, capacidade=capacidade)
            self.centro.adicionar_caminhao(caminhao)
            messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Capacidade deve ser um número.")

    def adicionar_entrega(self):
        destinatario = self.entry_destinatario.get()
        endereco = self.entry_endereco.get()
        
        if not destinatario or not endereco:
            messagebox.showerror("Erro", "Destinatário e Endereço são obrigatórios.")
            return
        
        entrega = Entrega(id=len(self.centro.entregas) + 1, destinatario=destinatario, endereco=endereco)
        self.centro.adicionar_entrega(entrega)
        messagebox.showinfo("Sucesso", "Entrega adicionada com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
