# def heapify(lista, tamanho, i):
#    maior = i
#    esquerda = 2 * i + 1
#    direita = 2 * i + 2
#
#    if esquerda < tamanho and lista[i] < lista[esquerda]:
#        maior = esquerda

#    if direita < tamanho and lista[maior] < lista[direita]:
#        maior = direita

#    if maior != i:
#         (lista[i], lista[maior]) = (lista[maior], lista[i])

#        heapify(lista, tamanho, maior)


# def heapsort(lista):
#     tamanho = len(lista)
#
#     for i in range(tamanho // 2 - 1, -1, -1):
#         heapify(lista, tamanho, i)
#
#     for i in range(tamanho - 1, 0, -1):
#         (lista[i], lista[0]) = (lista[0], lista[i])
#         heapify(lista, i, 0)

# O algoritmo de ordenação heapsort utiliza a estrutura de dados heap para ordenar um conjunto de elementos. A ideia
# básica do algoritmo é converter a sequência a ser ordenada em uma heap, que é uma árvore binária quase completa na
# qual cada nó é maior ou igual aos seus filhos (heap máximo) ou menor ou igual aos seus filhos (heap mínimo).

# A partir daí, o algoritmo realiza a ordenação em duas etapas: na primeira etapa, os elementos da sequência são
# colocados em uma heap máxima. Em seguida, o elemento raiz (maior elemento) é removido e colocado na última posição
# da sequência, que é então reduzida em uma unidade. O processo é repetido até que todos os elementos tenham sido
# removidos da heap. O resultado é uma sequência ordenada em ordem decrescente.

# Na segunda etapa, a sequência é novamente transformada em uma heap máxima, exceto que desta vez o maior elemento já
# está na posição correta. O processo é então repetido até que todos os elementos tenham sido removidos da heap.
# O resultado é uma sequência ordenada em ordem crescente.

# A complexidade de tempo do heapsort é O(n log n), tanto no pior caso quanto no caso médio, tornando-o um dos
# algoritmos de ordenação mais eficientes.

# def heapsort(lista):
#    tam_heap = len(lista)
#    for i in range(len(lista)//2, 0, -1):
#        lista = maxheapify(lista, i, tam_heap)
#
#    for i in range(len(lista)-1, 0, -1):
#        lista[0], lista[i] = lista[i], lista[0]
#        tam_heap -= 1
#        lista = maxheapify(lista, 1, tam_heap)
#
#    return lista


# def maxheapify(lista, no, tam_heap):
#    esquerda = no * 2
#    direita = no * 2 + 1
#    maior = no
#
#    if esquerda <= tam_heap and lista[esquerda-1] >= lista[no-1]:
#        maior = esquerda
#    if direita <= tam_heap and lista[direita-1] >= lista[maior-1]:
#        maior = direita
#    if maior != no:
#        lista[no-1], lista[maior-1] = lista[maior-1], lista[no-1]
#        maxheapify(lista, maior, tam_heap)
#    return lista


def heap(lista):
    tam_heap = len(lista)
    for i in range(tam_heap//2 - 1, -1, -1):
        max_heapify(lista, i)


def max_heapify(lista, no):
    esquerda = no * 2
    direita = no * 2 + 1
    if esquerda < len(lista) and lista[esquerda] > lista[no]:
        maior = esquerda
    else:
        maior = no
    if direita < len(lista) and lista[direita] > lista[maior]:
        maior = direita
    if maior != no:
        lista[no], lista[maior] = lista[maior], lista[no]
        max_heapify(lista, maior)


def minimo(lista):
    tam_heap = len(lista)
    menor = lista[tam_heap // 2]
    if tam_heap == 1:
        return lista[0]
    else:
        for i in range(1 + tam_heap // 2, tam_heap):  # percorre as folhas
            if menor > lista[i]:
                menor = lista[i]

    return menor


seq_num = list(map(int, input().split()))
constante = int(input())

heap(seq_num)

partida = True
qntd_partidas = 0

while partida:
    maxim = seq_num[0]
    minin = minimo(seq_num)

    seq_num.pop(0)
    k = maxim - (minin * constante)

    if k > 0:
        seq_num.append(k)
        heap(seq_num)

    if len(seq_num) == 0:
        partida = False

    qntd_partidas += 1

print(f'{qntd_partidas} rodadas, partindo para a próxima!')
