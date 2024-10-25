
class No:
    def __init__(self, dado, prox=None):
        self.dado = dado
        self.prox = prox

    def get_data(self):
        return self.dado

    def set_data(self, novo_dado):
        self.dado = novo_dado


class ListaEnc:
    def __init__(self):
        self.header = No(None)
        self.tail = self.header
        self.tamanho = 0

    def inserir_inicio(self, elemento):
        novo_no = No(elemento)
        novo_no.prox = self.header.prox
        self.header.prox = novo_no
        if self.tail == self.header:
            self.tail = novo_no
        self.tamanho += 1

    def inserir_depois(self, no_anterior, elemento):
        novo_no = No(elemento)
        novo_no.prox = no_anterior.prox
        no_anterior.prox = novo_no
        if self.tail == no_anterior:
            self.tail = novo_no
        self.tamanho += 1

    def inserir_final(self, elemento):
        novo_no = No(elemento)
        self.tail.prox = novo_no
        self.tail = novo_no
        self.tamanho += 1

    def print_lista(self):
        el = self.header.prox
        lista = []
        while el is not None:
            lista.append(el.dado)
            el = el.prox
        return lista

    def reorganizacao(self, fila):
        tamanho = self.tamanho
        metade = round(tamanho / 2)
        el = self.header.prox
        deslocados = []

        contador = 0
        while el is not None:
            if contador >= metade:
                deslocados.append(el.dado)
            el = el.prox
            contador += 1

        for el_ in reversed(deslocados):
            if fila.tamanho == 0:
                fila.inserir_inicio(el_)
                self.remover_ultimo()
            else:
                fila.inserir_final(el_)
                self.remover_ultimo()

    def remover_primeiro(self):
        primeiro = self.header.prox
        self.header.prox = primeiro.prox
        if self.tail == primeiro:
            self.tail = self.header
        self.tamanho -= 1
        return primeiro.dado

    def remover_ultimo(self):
        posicao = self.header.prox
        anterior = self.header
        while posicao.prox is not None:
            anterior = posicao
            posicao = posicao.prox
        if self.tail == posicao:
            self.tail = anterior
        anterior.prox = None
        self.tamanho -= 1
        return posicao.dado


programa = False

fila1 = ListaEnc()
fila2 = ListaEnc()

valores_caixa1 = ListaEnc()
valores_caixa2 = ListaEnc()

t1 = 0.0
t2 = 0.0

lista_comandos = ['ENTROU:', 'PROXIMO:', 'FIM']

while not programa:
    interface = input().split()  # acão, cliente, caixa, total$
    if interface[0] == lista_comandos[2]:

        print(f'Caixa 1: R$ {t1:.2f}, Caixa 2: R$ {t2:.2f}')
        break

    else:
        if interface[0] == lista_comandos[0]:
            if interface[2] == '1' and fila1.tamanho == 0:
                fila1.inserir_inicio(interface[1])

                dinheiro_float = float(interface[3])
                valores_caixa1.inserir_inicio(dinheiro_float)

            elif interface[2] == '1':
                fila1.inserir_final(interface[1])

                dinheiro_float = float(interface[3])
                valores_caixa1.inserir_final(dinheiro_float)

            elif interface[2] == '2' and fila2.tamanho == 0:
                fila2.inserir_inicio(interface[1])

                dinheiro_float = float(interface[3])
                valores_caixa2.inserir_inicio(dinheiro_float)

            elif interface[2] == '2':
                fila2.inserir_final(interface[1])

                dinheiro_float = float(interface[3])
                valores_caixa2.inserir_final(dinheiro_float)

            print(f'{interface[1]} entrou na fila {interface[2]}')

        elif interface[0] == lista_comandos[1]:

            if interface[1] == '1' and fila1.tamanho == 0:
                fila2.reorganizacao(fila1)
                valores_caixa2.reorganizacao(valores_caixa1)

                print(f'{fila1.header.prox.dado} foi chamado para o caixa {interface[1]}')

                fila1.remover_primeiro()
                t1 += valores_caixa1.header.prox.dado
                valores_caixa1.remover_primeiro()

            elif interface[1] == '1':
                print(f'{fila1.header.prox.dado} foi chamado para o caixa {interface[1]}')

                fila1.remover_primeiro()
                t1 += valores_caixa1.header.prox.dado
                valores_caixa1.remover_primeiro()

            elif interface[1] == '2' and fila2.tamanho == 0:
                fila1.reorganizacao(fila2)
                valores_caixa1.reorganizacao(valores_caixa2)

                print(f'{fila2.header.prox.dado} foi chamado para o caixa {interface[1]}')

                fila2.remover_primeiro()
                t2 += valores_caixa2.header.prox.dado
                valores_caixa2.remover_primeiro()

            elif interface[1] == '2':
                print(f'{fila2.header.prox.dado} foi chamado para o caixa {interface[1]}')

                fila2.remover_primeiro()
                t2 += valores_caixa2.header.prox.dado
                valores_caixa2.remover_primeiro()
