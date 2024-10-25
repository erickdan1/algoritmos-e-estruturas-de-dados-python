class No:
    def __init__(self, dado, pai=None):
        self.dado = dado
        self.filho_esq = None
        self.filho_dir = None
        self.pai = pai
        self.altura = 0


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        # se a raiz não existir
        if not self.raiz:
            self.raiz = No(dado)
            print(f'{dado} INSERIDO')

        else:
            self.inserir_dado(dado, self.raiz)
            print(f'{dado} INSERIDO')

    def remover(self, dado):
        if not self.raiz:
            '''print(f'{dado} NAO ENCONTRADO')'''
        else:
            self.remover_dado(dado, self.raiz)

    def inserir_dado(self, dado, no):
        if dado < no.dado:
            if no.filho_esq:
                self.inserir_dado(dado, no.filho_esq)
            else:
                no.filho_esq = No(dado, no)
                self.manipulador_violacao(no.filho_esq)
        if dado > no.dado:
            if no.filho_dir:
                self.inserir_dado(dado, no.filho_dir)
            else:
                no.filho_dir = No(dado, no)
                self.manipulador_violacao(no.filho_dir)

    def remover_dado(self, dado, no):
        if dado < no.dado:
            if no.filho_esq:
                self.remover_dado(dado, no.filho_esq)
        elif dado > no.dado:
            if no.filho_dir:
                self.remover_dado(dado, no.filho_dir)
        elif dado == no.dado:
            # se for uma folha
            if not no.filho_esq and not no.filho_dir:
                no_pai = no.pai
                if no_pai:
                    if no_pai.filho_esq == no:
                        no_pai.filho_esq = None
                    elif no_pai.filho_dir == no:
                        no_pai.filho_dir = None
                # se for raiz
                else:
                    self.raiz = None
                del no
                print(f'{dado} DELETADO')
                self.manipulador_violacao(no_pai)
            # se o filho a esquerda existir
            elif no.filho_esq and not no.filho_dir:
                no_pai = no.pai

                if no_pai:
                    if no_pai.filho_esq == no:
                        no_pai.filho_esq = no.filho_esq
                    elif no_pai.filho_dir == no:
                        no_pai.filho_dir = no.filho_esq
                else:
                    self.raiz = no.filho_esq

                no.filho_esq.pai = no_pai
                del no
                print(f'{dado} DELETADO')
                self.manipulador_violacao(no_pai)
            # se o filho a direita existir
            elif no.filho_dir and not no.filho_esq:
                no_pai = no.pai

                if no_pai:
                    if no_pai.filho_esq == no:
                        no_pai.filho_esq = no.filho_dir
                    elif no_pai.filho_dir == no:
                        no_pai.filho_dir = no.filho_dir
                else:
                    self.raiz = no.filho_dir

                no.filho_dir.pai = no_pai
                del no
                print(f'{dado} DELETADO')
                self.manipulador_violacao(no_pai)
            # se o nó tiver os dois filhos
            elif no.filho_esq and no.filho_dir:
                no_sucessor = self.sucessor(no.filho_dir)
                no_sucessor.dado, no.dado = no.dado, no_sucessor.dado
                self.remover_dado(no_sucessor.dado, no.filho_dir)

    def sucessor(self, no):
        if no.filho_esq:
            return self.sucessor(no.filho_esq)
        return no

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

        temp_parent = no.pai
        temp_filho_dir.pai = temp_parent
        no.pai = temp_filho_dir
        if t:
            t.pai = no

        if temp_filho_dir.pai:   # se não for a raiz
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

        temp_parent = no.pai
        temp_filho_esq.pai = temp_parent
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
            print('ARVORE VAZIA')
            return False

    def em_ordem_(self, no):
        if no.filho_esq:
            self.em_ordem_(no.filho_esq)

        elementos_emordem.append(no.dado)

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
            return True
        return False

    def minimo(self):
        if self.raiz:
            return self.buscar_minimo(self.raiz)
        else:
            return 'ARVORE VAZIA'

    def buscar_minimo(self, no):
        if no.filho_esq:
            return self.buscar_minimo(no.filho_esq)
        return f'MENOR: {no.dado}'

    def maximo(self):
        if self.raiz:
            return self.buscar_maximo(self.raiz)
        else:
            return 'ARVORE VAZIA'

    def buscar_maximo(self, no):
        if no.filho_dir:
            return self.buscar_maximo(no.filho_dir)
        return f'MAIOR: {no.dado}'


arvore_avl = ArvoreAVL()

elementos_emordem = []  # variavel global para impressão dos elementos

programa = True

while programa:
    comando = input().split()

    if comando[0] == 'INSERIR':
        if arvore_avl.buscar(comando[1]):
            print(f'{comando[1]} JA EXISTE')
        else:
            arvore_avl.inserir(comando[1])

    elif comando[0] == 'DELETAR':
        if arvore_avl.buscar(comando[1]):
            arvore_avl.remover(comando[1])
        else:
            print(f'{comando[1]} NAO ENCONTRADO')

    elif comando[0] == 'MINIMO':
        print(arvore_avl.minimo())

    elif comando[0] == 'MAXIMO':
        print(arvore_avl.maximo())

    elif comando[0] == 'ALTURA':
        print(f'ALTURA: {arvore_avl.altura_arvore() + 1}')

    elif comando[0] == 'FIM':
        if arvore_avl.percorrer():
            em_ordem = ' '.join(map(str, elementos_emordem))
            print(em_ordem)

        programa = False
