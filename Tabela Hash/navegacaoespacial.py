# Uma tabela hash é uma estrutura de dados especial, que associa chaves de pesquisa a valores, através de uma função.
# Seu objetivo é, a partir de uma chave simples, fazer uma busca rápida e obter o valor desejado
class TabelaHash:
    def __init__(self, tam_max):
        self.tabela = {}
        self.tam_max = tam_max

    def funcao_hash(self, chave):
        return chave % self.tam_max  # código do dado % tamanho da tabela

    def adicionar(self, chave):
        posicao = self.funcao_hash(chave)
        if self.tabela.get(posicao) is None:  # se posicao vazia
            self.tabela[posicao] = chave
            return f'E: {posicao}'
        else:
            nova_posicao = self.novo_posicao(posicao)
            return f'E: {nova_posicao}'

    def buscar(self, chave):
        posicao = self.funcao_hash(chave)
        if self.tabela.get(posicao) is None or self.tabela.get(posicao) != chave:
            return 'NE'
        else:
            return f'E: {posicao}'

    def cheio(self):
        return self.tam_max == len(self.tabela)

    def cap(self, posicao):
        if self.tabela.get(posicao) is None:  # quando estiver disponível
            return 'D'
        else:
            return f'A: {self.tabela.get(posicao)}'

    def novo_posicao(self, pos_ante):
        posicao = pos_ante
        while True:
            if self.tabela.get(posicao) is None:
                return posicao
            else:
                if posicao < self.tam_max:
                    posicao += 1
                else:
                    posicao = 0


tamanho_tabela = int(input())

tabela_hash = TabelaHash(tamanho_tabela)

qntd_comandos = int(input())

for i in range(qntd_comandos):
    comando, xmd = input().split()
    xmd_int = int(xmd)

    if tabela_hash.cheio():
        print('Toda memoria utilizada')
        break

    elif comando == 'ADD':
        print(tabela_hash.adicionar(xmd_int))

    elif comando == 'SCH':
        print(tabela_hash.buscar(xmd_int))

    elif comando == 'CAP':
        print(tabela_hash.cap(xmd_int))
