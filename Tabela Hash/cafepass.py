# Pode usar lista (Python List)
# Não pode usar dicionário (Python dict)
# Atenção com o uso excessivo de trechos com O(nˆ2)
# Obrigatório usar Tabela Hash
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, val):
        ind = 0
        posicao = self.funcao_hash(chave)
        while ind < len(self.tabela):
            if self.tabela[posicao] is None:
                self.tabela[posicao] = [chave, val]  # insere como lista
            else:
                ind += 1
                posicao = (posicao + 1) % len(self.tabela)


def transformar_cpf(numero_cpf):
    # multiplica os digitos por 10 e transforma numa lista
    lista_cpf = []
    for digito in numero_cpf:
        lista_cpf.append(int(digito) * 10)

    lista_cpf_aux = lista_cpf[:]  # lista auxiliar (cópia da lista "lista_cpf")
    # verifica se tem dígitos repetidos e os soma
    for el in range(len(lista_cpf)):
        for elem in range(el + 1, len(lista_cpf)):
            if lista_cpf[el] == lista_cpf[elem]:
                lista_cpf_aux[el] += lista_cpf[elem]
                lista_cpf[elem] = 0
                lista_cpf_aux[elem] = 0
    # remove os dígitos repetidos que viraram zeros quando foram somados
    lista_cpf_ok = []
    if '0' in numero_cpf:  # adicionar o zero e evitar que ele seja apagado
        lista_cpf_ok.append(0)
    for digito in lista_cpf_aux:
        if digito != 0:
            lista_cpf_ok.append(digito)

    return lista_cpf_ok


def permissao(lista_num, magic_number):
    ja_vistos = []  # números já vistos
    for n in lista_num:
        # se algum número visto anteriormente soma para o valor desejado
        diferenca = magic_number - n
        if diferenca in ja_vistos:
            return True
        ja_vistos.append(n)
    return False


tabela_hash = TabelaHash(1000)

num = int(input())

for i in range(num):
    cpf, magic_num_str = input().split()
    magic_num = int(magic_num_str)

    lista = transformar_cpf(cpf)
    if len(cpf) == 11 and 3 <= magic_num <= 990:
        if permissao(lista, magic_num):
            print('UP Permission')
            tabela_hash.inserir(int(cpf), True)  # associa o número de cpf a se ele é autorizado (True) ou não (False)
        else:                                    # numa lista, e adciona à tabela hash
            print('NOT Permission')
            tabela_hash.inserir(int(cpf), False)
