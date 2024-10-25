
# def merge(esquerda, direita):
#    index_esq, index_dir = 0, 0
#    resultado = []
#    while index_esq < len(esquerda) and index_dir < len(direita):
#        if esquerda[index_esq] < direita[index_dir]:
#            resultado.append(esquerda[index_esq])
#            index_esq += 1
#        else:
#            resultado.append(direita[index_dir])
#            index_dir += 1
#
#    resultado += esquerda[index_esq:]
#    resultado += direita[index_dir:]
#    return resultado


# def merge_sort(lista):
#    if len(lista) <= 1:
#        return lista

#    meio = len(lista) // 2
#    esquerda = merge_sort(lista[:meio])
#    direita = merge_sort(lista[meio:])

#    return merge(esquerda, direita)

# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html


def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i = i+1
            else:
                lista[k] = direita[j]
                j = j+1
            k = k+1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i = i+1
            k = k+1

        while j < len(direita):
            lista[k] = direita[j]
            j = j+1
            k = k+1


def unir(lista1, lista2):
    salarios = []
    salarios.extend(lista1)
    salarios.extend(lista2)
    return salarios


def mediana(lista):
    tamanho = len(lista)
    if tamanho % 2 == 0:
        meio = tamanho // 2
        return (lista[meio] + lista[(meio - 1)]) / 2
    else:
        return lista[tamanho // 2]


salarios_sport = list(map(int, input().split()))
salarios_futclube = list(map(int, input().split()))

uniao = unir(salarios_sport, salarios_futclube)

merge_sort(uniao)

print(f'O salário sugerido por Juba na primeira negociação será de {mediana(uniao):.2f} mil reais.')
