class No:
    def __init__(self, dado):
        self.dado = dado
        self.filho_esq = None
        self.filho_dir = None
        self.pai = None
        self.altura = 0


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            pai = None
            no_atual = self.raiz
            while no_atual is not None:
                pai = no_atual
                if dado < no_atual.dado:
                    no_atual = no_atual.filho_esq
                else:
                    no_atual = no_atual.filho_dir

            novo_no.pai = pai
            if dado < pai.dado:
                pai.filho_esq = novo_no
            else:
                pai.filho_dir = novo_no

    def mover_topo(self, dado):
        no = self.buscar(dado)
        return self.mover(no)

    def mover(self, no):
        # se a raiz já é o nó
        if no == self.raiz:
            return

        # encontrar caminho da raiz até o nó
        caminho = []
        no_atual = self.raiz
        while no_atual != no:
            caminho.append(no_atual)
            if no.dado < no_atual.dado:
                no_atual = no_atual.filho_esq
            else:
                no_atual = no_atual.filho_dir

        # remover nó da posição atual
        pai = caminho[-1]
        if pai.filho_esq == no:
            pai.filho_esq = None
        else:
            pai.filho_dir = None

        # agregar o nó à raiz
        no.filho_esq = no.filho_dir = None
        no_atual = self.raiz
        while no_atual:
            if no.dado < no_atual.dado:
                if no_atual.filho_esq is None:
                    no_atual.filho_esq = no
                    break
                else:
                    no_atual = no_atual.filho_esq
            else:
                if no_atual.filho_dir is None:
                    no_atual.filho_dir = no
                    break
                else:
                    no_atual = no_atual.filho_dir

        # atualiza a raiz
        self.raiz = no

        # balanceia a arvore
        return self.manipulador_violacao(self.raiz)

    def manipulador_violacao(self, no):
        while no:
            no.altura = max(self.calcular_altura(no.filho_esq), self.calcular_altura(no.filho_dir)) + 1
            self.ajustar_violacao(no)
            no = no.pai

    def altura_arvore(self):
        if self.raiz:
            return self.calcular_altura(self.raiz)

    def calcular_altura(self, no):
        # A altura de um nó qualquer é o valor máximo entre a altura do nó a sua direita e
        # do nó a sua esquerda, somado 1.
        if not no:
            return -1
        return no.altura

    def ajustar_violacao(self, no):
        if self.fator_balaceamento(no) > 1:
            if self.fator_balaceamento(no.filho_esq) < 0:
                self.rotacao_esquerda(no.filho_esq)
            self.rotacao_direita(no)

        if self.fator_balaceamento(no) < -1:
            if self.fator_balaceamento(no.filho_dir) > 0:
                self.rotacao_direita(no.filho_dir)
            self.rotacao_esquerda(no)

    def fator_balaceamento(self, no):
        if not no:
            return 0
        return self.calcular_altura(no.filho_esq) - self.calcular_altura(no.filho_dir)

    def rotacao_esquerda(self, no):
        temp_filho_dir = no.filho_dir
        t = no.filho_dir.filho_esq

        temp_filho_dir.filho_esq = no
        no.filho_dir = t

        temp_pai = no.pai
        temp_filho_dir.pai = temp_pai
        no.pai = temp_filho_dir
        if t:
            t.pai = no

        if temp_filho_dir.pai:  # se não for a raiz
            if temp_filho_dir.pai.filho_esq == no:
                temp_filho_dir.pai.filho_esq = temp_filho_dir
            elif temp_filho_dir.pai.filho_dir == no:
                temp_filho_dir.pai.filho_dir = temp_filho_dir
        # se for a raiz
        else:
            self.raiz = temp_filho_dir

        # atualizar altura
        no.altura = max(self.calcular_altura(no.filho_esq), self.calcular_altura(no.filho_dir)) + 1
        temp_filho_dir.altura = max(self.calcular_altura(temp_filho_dir.filho_esq),
                                    self.calcular_altura(temp_filho_dir.filho_dir)) + 1

    def rotacao_direita(self, no):
        temp_filho_esq = no.filho_esq
        t = no.filho_esq.filho_dir

        temp_filho_esq.filho_dir = no
        no.filho_esq = t

        temp_pai = no.pai
        temp_filho_esq.pai = temp_pai
        no.pai = temp_filho_esq
        if t:
            t.pai = no

        if temp_filho_esq.pai:
            if temp_filho_esq.pai.filho_esq == no:
                temp_filho_esq.pai.filho_esq = temp_filho_esq
            elif temp_filho_esq.pai.filho_dir == no:
                temp_filho_esq.pai.filho_dir = temp_filho_esq
        else:
            self.raiz = temp_filho_esq

        # atualizar altura
        no.altura = max(self.calcular_altura(no.filho_esq), self.calcular_altura(no.filho_dir)) + 1
        temp_filho_esq.altura = max(self.calcular_altura(temp_filho_esq.filho_esq),
                                    self.calcular_altura(temp_filho_esq.filho_dir)) + 1

    def percorrer(self):
        if self.raiz:
            self.em_ordem_(self.raiz)
            return True
        else:
            return False

    def em_ordem_(self, no):
        if no.filho_esq:
            self.em_ordem_(no.filho_esq)

        print(no.dado)

        if no.filho_dir:
            self.em_ordem_(no.filho_dir)

    def buscar(self, dado):
        if self.raiz:
            return self.buscar_dado(dado, self.raiz)

    def buscar_dado(self, dado, no):
        if dado < no.dado:
            if no.filho_esq:
                return self.buscar_dado(dado, no.filho_esq)
        elif dado > no.dado:
            if no.filho_dir:
                return self.buscar_dado(dado, no.filho_dir)
        elif dado == no.dado:
            return no
        return False


def buscar_nivel(raiz, dado, nivel=0):
    if raiz is None:  # se a raiz não existe
        return None

    if raiz.dado == dado:  # se for a raiz
        return nivel
    else:  # recursao de procura
        nivel_esq = buscar_nivel(raiz.filho_esq, dado, nivel + 1)
        if nivel_esq is not None:
            return nivel_esq
        else:
            nivel_dir = buscar_nivel(raiz.filho_dir, dado, nivel + 1)
            return nivel_dir


arvore_binaria = ArvoreBinaria()

while True:
    try:
        operacoes = input().split()
        numero = int(operacoes[1])

        # Current Level
        if operacoes[0] == 'ADD':  # adicionar e printar o nível em que o dado foi inserido (CL)
            arvore_binaria.inserir(numero)
            '''arvore_binaria.percorrer()'''
            print(buscar_nivel(arvore_binaria.raiz, numero, 0))

        # Previous Level
        elif operacoes[0] == 'SCH':  # printar o nível em que o dado estava antes de ir ao topo (PL)
            if arvore_binaria.buscar(numero):
                print(buscar_nivel(arvore_binaria.raiz, numero, 0))
                arvore_binaria.mover_topo(numero)
            else:
                print('-1')
    except EOFError:
        break
