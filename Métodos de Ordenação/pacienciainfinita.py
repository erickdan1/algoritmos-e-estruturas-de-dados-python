def bubblesort(lista, lim=None):
    global comparacoes_bubble, trocas_bubble
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes_bubble += 1
            if lim == (comparacoes_bubble + trocas_bubble):
                return lista
            if lista[j] > lista[j + 1]:
                if lim == (comparacoes_bubble + trocas_bubble):
                    return lista
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas_bubble += 1
                if lim == (comparacoes_bubble + trocas_bubble):
                    return lista
    return lista


def selection_sort(lista, lim=None):
    global comparacoes_selection, trocas_selection
    comprimento = len(lista)

    for i in range(comprimento - 1):
        min_index = i

        for j in range(i + 1, comprimento):
            if lim == (comparacoes_selection + trocas_selection):
                return lista
            comparacoes_selection += 1
            if lim == (comparacoes_selection + trocas_selection):
                return lista
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]
        if lista[min_index] != lista[i]:
            if lim == (comparacoes_selection + trocas_selection):
                return lista
            trocas_selection += 1
            if lim == (comparacoes_selection + trocas_selection):
                return lista
    return lista


def insertion_sort(lista, lim=None):
    global comparacoes_insertion, trocas_insertion

    for i in range(1, len(lista)):
        if lim == (comparacoes_insertion + trocas_insertion):
            return lista
        valor = lista[i]

        j = i - 1
        while True:
            if lim == (comparacoes_insertion + trocas_insertion):
                return lista
            if j >= 0 and valor < lista[j]:
                if lim == (comparacoes_insertion + trocas_insertion):
                    return lista
                lista[j + 1] = lista[j]
                j -= 1
                trocas_insertion += 1
                if lim == (comparacoes_insertion + trocas_insertion):
                    return lista
                comparacoes_insertion += 1
                if lim == (comparacoes_insertion + trocas_insertion):
                    return lista

            elif valor >= lista[j] and j >= 0:
                comparacoes_insertion += 1
                if lim == (comparacoes_insertion + trocas_insertion):
                    return lista
                break

            else:
                break
        if lim == (comparacoes_insertion + trocas_insertion):
            return lista
        lista[j + 1] = valor

    return lista


def shell_sort(lista, n, lim=None):
    global comparacoes_shell, trocas_shell
    lista_aux = lista[:]

    intervalo = n // 2
    while intervalo > 0:
        if lim == (comparacoes_shell + trocas_shell):
            return lista_aux
        for i in range(intervalo, n):
            if lim == (comparacoes_shell + trocas_shell):
                return lista_aux
            temp = lista_aux[i]
            j = i
            while True:
                if j >= intervalo and lista_aux[j - intervalo] > temp:
                    if lim == (comparacoes_shell + trocas_shell):
                        return lista_aux
                    lista_aux[j] = lista_aux[j - intervalo]
                    trocas_shell += 1
                    if lim == (comparacoes_shell + trocas_shell):
                        return lista_aux
                    comparacoes_shell += 1
                    if lim == (comparacoes_shell + trocas_shell):
                        return lista_aux
                    j -= intervalo

                elif lista_aux[j - intervalo] <= temp:
                    comparacoes_shell += 1
                    if lim == (comparacoes_shell + trocas_shell):
                        return lista_aux
                    break

                else:
                    break
            if lim == (comparacoes_shell + trocas_shell):
                return lista_aux
            lista_aux[j] = temp
        intervalo //= 2
    return lista_aux


def quicksort_isa(a, lo, hi, lim=None):

    if 0 <= lo < hi and hi >= 0:
        p = partition(a, lo, hi, lim)
        quicksort_isa(a, lo, p)
        quicksort_isa(a, p + 1, hi)


def partition(a, lo, hi, lim):
    global comparacoes_quick, trocas_quick
    pivot = a[(hi + lo) // 2]
    i = lo
    j = hi

    while True:
        if i >= j:
            return j
        while a[i] < pivot:
            if lim == (comparacoes_quick + trocas_quick):
                return a
            i += 1
            comparacoes_quick += 1
        while a[j] > pivot:
            if lim == (comparacoes_quick + trocas_quick):
                return a
            j -= 1
            comparacoes_quick += 1

        a[i], a[j] = a[j], a[i]
        trocas_quick += 1


livros = [int(i) for i in input().split()]

# primeira etapa
# Caça Rato (BubbleSort)
comparacoes_bubble = 0
trocas_bubble = 0


def cacarato(etapa=1):
    if etapa == 1:
        sort_cacarato = bubblesort(livros[:])

        print(f'Caça-Rato ordena a lista com {comparacoes_bubble} comparações e {trocas_bubble} trocas.')

        return sort_cacarato
    elif etapa == 2:
        sort_cacarato = bubblesort(livros[:], menor_pontuacao)

        print(f'Com {menor_pontuacao} ações, Caça-Rato ordena a lista assim: {sort_cacarato}')


cacarato()
soma_cacarato = comparacoes_bubble + trocas_bubble

# Grafite (SelectionSort)
comparacoes_selection = 0
trocas_selection = 0


def grafite(etapa=1):
    if etapa == 1:
        sort_grafite = selection_sort(livros[:])

        print(f'Grafite ordena a lista com {comparacoes_selection} comparações e {trocas_selection} trocas.')

        return sort_grafite
    elif etapa == 2:
        sort_grafite = selection_sort(livros[:], menor_pontuacao)

        print(f'Com {menor_pontuacao} ações, Grafite ordena a lista assim: {sort_grafite}')


grafite()
soma_grafite = comparacoes_selection + trocas_selection

# Lacraia (InsertionSort)

comparacoes_insertion = 0
trocas_insertion = 0


def lacraia(etapa=1):
    if etapa == 1:
        sort_lacraia = insertion_sort(livros[:])

        print(f'Lacraia ordena a lista com {comparacoes_insertion} comparações e {trocas_insertion} trocas.')

        return sort_lacraia
    elif etapa == 2:
        sort_lacraia = insertion_sort(livros[:], menor_pontuacao)

        print(f'Com {menor_pontuacao} ações, Lacraia ordena a lista assim: {sort_lacraia}')


lacraia()
soma_lacraia = comparacoes_insertion + trocas_insertion

# Rivaldo (ShellSort)
comparacoes_shell = 0
trocas_shell = 0


def rivaldo(etapa=1):
    if etapa == 1:
        sort_rivaldo = shell_sort(livros, len(livros))

        print(f'Rivaldo ordena a lista com {comparacoes_shell} comparações e {trocas_shell} trocas.')

        return sort_rivaldo
    elif etapa == 2:
        sort_rivaldo = shell_sort(livros, len(livros), menor_pontuacao)

        print(f'Com {menor_pontuacao} ações, Rivaldo ordena a lista assim: {sort_rivaldo}')


rivaldo()
soma_rivaldo = comparacoes_shell + trocas_shell

# Toninho (QuickSort (Hoare partition))
comparacoes_quick = 0
trocas_quick = 0


def toninho(etapa=1):
    if etapa == 1:
        sort_toninho = livros[:]

        quicksort_isa(sort_toninho, 0, len(sort_toninho) - 1)

        print(f'Toninho ordena a lista com {comparacoes_quick} comparações e {trocas_quick} trocas.')

        return sort_toninho
    elif etapa == 2:
        sort_toninho = livros[:]

        quicksort_isa(sort_toninho, 0, len(sort_toninho) - 1, menor_pontuacao)

        print(f'Com {menor_pontuacao} ações, Toninho ordena a lista assim: {sort_toninho}')


toninho()
soma_toninho = comparacoes_quick + trocas_quick

# Vencedor
pontuacoes = [['Caça-Rato', soma_cacarato], ['Grafite', soma_grafite], ['Lacraia', soma_lacraia],
              ['Rivaldo', soma_rivaldo], ['Toninho', soma_toninho]]
menor_pontuacao = min(soma_cacarato, soma_grafite, soma_lacraia, soma_rivaldo, soma_toninho)

vencedor_q_sai = ''
participantes_segunda_etapa = []
print('-VENCEDOR DA RODADA-')
for i in range(len(pontuacoes)):
    if pontuacoes[i][1] == menor_pontuacao:
        print(f'O vencedor da rodada é {pontuacoes[i][0]}, com {menor_pontuacao} ações.')
        vencedor_q_sai = pontuacoes[i][0]
    else:
        participantes_segunda_etapa.append(pontuacoes[i][0])

comparacoes_bubble = 0
comparacoes_selection = 0
comparacoes_quick = 0
comparacoes_shell = 0
comparacoes_insertion = 0

trocas_bubble = 0
trocas_selection = 0
trocas_quick = 0
trocas_shell = 0
trocas_insertion = 0

# segunda etapa
# Toninho nao vai participar
print('-Toninho está a dormir...-')
print('Os outros estagiários retornam as seguintes listas com essa quantidade de ações:')

if 'Caça-Rato' in participantes_segunda_etapa:
    cacarato(2)
if 'Grafite' in participantes_segunda_etapa:
    grafite(2)
if 'Lacraia' in participantes_segunda_etapa:
    lacraia(2)
if 'Rivaldo' in participantes_segunda_etapa:
    rivaldo(2)

'''
# fazendo Toninho participar
if 'Toninho' in participantes_segunda_etapa:
    toninho(2)
'''
