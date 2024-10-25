# a inserção no final de uma lista encadeada tem complexidade O(n).
# Uma maneira de melhorar essa operação consiste na definição de listas duplamente encadeadas.
# Em listas duplamente encadeadas, tanto a inserção quanto a remoção no final são operações O(1).

# Classe do Nó
class No:
    def __init__(self, init_data, ante, prox):
        self.data = init_data
        self.ante = ante        # direções para onde apontam
        self.prox = prox        # inicialmente não aponta pra ninguém

    # obter dado armazenado
    def get_data(self):
        return self.data

    # atualizar dado armazenado
    def set_data(self, new_data):
        self.data = new_data


class ListaDuplaEnc:
    def __init__(self):
        self.header = No(None, None, None)  # o nó que indica o início da lista
        self.trailer = No(None, None, None)  # o nó que indica o fim da lista

        self.header.prox = self.trailer  # header aponta seu ponteiro de próximo para trailer
        self.trailer.ante = self.header  # trailer aponta o ponteiro de anterior para header

        self.tamanho = 0

    #  verifica se a lista está vazia
    def lista_vazia(self):
        return self.tamanho == 0

    #  retornar o número de elementos da lista
    def __len__(self):
        return self.tamanho

    # inserir novo nó entre dois já existentes
    def inserir_entre(self, item, predecessor, sucessor):
        novo = No(item, predecessor, sucessor)
        predecessor.prox = novo
        sucessor.ante = novo
        self.tamanho += 1
        return novo

    #  Remove um nó intermediário da lista
    #  Obs: Header e Trailer nunca podem ser removidos
    def apagar_no(self, no):
        predecessor = no.ante
        sucessor = no.prox
        predecessor.prox = sucessor
        sucessor.ante = predecessor
        self.tamanho -= 1

        # armazena elemento removido
        elemento = no.data
        no.ante = no.prox = no.elemento = None
        return elemento

    #  insere elemento no início
    def inserir_primeiro(self, data):
        # nó deve entrar entre header e header.prox
        self.inserir_entre(data, self.header, self.header.prox)

    #  insere elemento no final
    def inserir_ultimo(self, data):
        self.inserir_entre(data, self.trailer.ante, self.trailer)

    #  remover primeiro nó
    def apagar_primeiro(self):
        if self.lista_vazia():
            print('Lista está vazia')
        else:
            return self.apagar_no(self.header.prox)

    #  remover último nó
    def apagar_ultimo(self):
        if self.lista_vazia():
            print('Lista está vazia')
        else:
            return self.apagar_no(self.trailer.ante)

    #  imprime elementos da lista
    def print_lista(self):
        # aponta referência para cabeça
        el = self.header.prox  # elemento
        x = []
        # percorre lista adicionando elementos em X
        while el.prox is not None:
            x.append(el.data)
            el = el.prox
        return x

    def buscar(self, elemento):
        percorrer = self.header.prox

        while percorrer:
            if percorrer.data == elemento:
                return percorrer
            percorrer = percorrer.prox

    def find(self, elemento):
        percorrer = self.header.prox

        while percorrer:
            if percorrer.data == elemento:
                return self.inserir_primeiro(percorrer.data), self.apagar_no(percorrer)

            percorrer = percorrer.prox


lista_duplamente_encadeada = ListaDuplaEnc()

programa = True
comandos = ['ADD', 'REM', 'EXIB', 'FIND', 'END']
while programa:
    comando = input().split()

    if comando[0] == comandos[0] and lista_duplamente_encadeada.lista_vazia():
        lista_duplamente_encadeada.inserir_primeiro(comando[1])
        print(lista_duplamente_encadeada.print_lista())

    elif comando[0] == comandos[0] and lista_duplamente_encadeada.lista_vazia() is not True:
        lista_duplamente_encadeada.inserir_entre(comando[1],
                                                 lista_duplamente_encadeada.header,
                                                 lista_duplamente_encadeada.header.prox)
        print(lista_duplamente_encadeada.print_lista())

    elif comando[0] == comandos[1]:
        remover = lista_duplamente_encadeada.buscar(comando[1])
        lista_duplamente_encadeada.apagar_no(remover)

        print(lista_duplamente_encadeada.print_lista())

    elif comando[0] == comandos[2]:
        historico = lista_duplamente_encadeada.print_lista()
        for i in historico:
            print(i)

    elif comando[0] == comandos[3]:
        lista_duplamente_encadeada.find(comando[1])
        print(lista_duplamente_encadeada.print_lista())

    elif comando[0] == comandos[4]:
        programa = False
