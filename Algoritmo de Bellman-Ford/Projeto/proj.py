import sys
import networkx as nx
import matplotlib.pyplot as plt

from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Menor Caminho - Bellman-Ford")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.vertice1Label = Label(self.segundoContainer, text="Vértice Início", font=self.fontePadrao)
        self.vertice1Label.pack(side=LEFT)

        self.vertice1 = Entry(self.segundoContainer)
        self.vertice1["width"] = 30
        self.vertice1["font"] = self.fontePadrao
        self.vertice1.pack(side=LEFT)

        self.vertice2Label = Label(self.terceiroContainer, text="Vértice Fim", font=self.fontePadrao)
        self.vertice2Label.pack(side=LEFT)

        self.vertice2 = Entry(self.terceiroContainer)
        self.vertice2["width"] = 30
        self.vertice2["font"] = self.fontePadrao
        self.vertice2.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Buscar"
        self.autenticar["font"] = ("Calibri", "10")
        self.autenticar["width"] = 15
        self.autenticar["command"] = self.programa
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Método verificar vertice2
    def programa(self):

        with open('CollegeMsg.txt', 'r') as banco_dados:
            header = next(banco_dados)
            vertices = set()
            for linha in banco_dados:
                dados = linha.split()
                u = int(dados[0])
                v = int(dados[1])
                peso = int(dados[2])
                vertices.add(u)
                vertices.add(v)
            vertices = len(vertices) + 1
            grafo = [[] for _ in range(vertices)]
            banco_dados.seek(0)
            next(banco_dados)
            for linha in banco_dados:
                dados = linha.split()
                u = int(dados[0])
                v = int(dados[1])
                peso = int(dados[2])
                grafo[u].append((v, peso))

        def bellman_ford(grafo, inicio, fim):
            # Inicializa o dicionário de distâncias
            dist = {v: sys.maxsize for v in range(len(grafo))}
            dist[inicio] = 0
            pred = [None] * len(grafo)

            # Loop principal do algoritmo de Bellman-Ford
            for i in range(len(grafo)-1):
                for u in range(len(grafo)):
                    for v, w in grafo[u]:
                        if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w
                            pred[v] = u

            # Verifica se há ciclos negativos no grafo
            for u in range(len(grafo)):
                for v, w in grafo[u]:
                    if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                        return "Grafo contém ciclos negativos"

            # Retorna o menor caminho e seus pesos
            caminho = [fim]
            while caminho[-1] != inicio:
                caminho.append(pred[caminho[-1]])
            return dist[fim], caminho[::-1]

        # Obter vértices de origem e destino do usuário

        inicio = int(self.vertice1.get())
        fim = int(self.vertice2.get())
        bf = bellman_ford(grafo, inicio, fim)[0]  # Imprime somente o tempo de reparo

        self.mensagem["text"] = f'\n Menor tempo em segundos: \n{bf}'

        ''' 
        G = nx.DiGraph()

        for u in range(len(grafo)):
            for v, w in grafo[u]:
                G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        fig, ax = plt.subplots(figsize=(80,60))
        nx.draw_networkx_nodes(G, pos, node_size=700, ax=ax)
        nx.draw_networkx_edges(G, pos, ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):d['weight'] for u,v,d in G.edges(data=True)}, ax=ax, font_size=15)
        ax.set_title('Grafo', fontsize=20)
        plt.axis('off')
        
        plt.show()
        
        
        
       '''


root = Tk()
Application(root)
root.mainloop()
