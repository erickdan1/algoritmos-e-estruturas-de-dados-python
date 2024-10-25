# O algoritmo de backtracking é uma técnica de busca sistemática que consiste em explorar todas as possibilidades para
# encontrar uma solução para um problema. Ele funciona de forma recursiva, testando todas as combinações possíveis para
# um determinado conjunto de elementos, e voltando atrás (backtracking) quando uma combinação não leva a uma solução
# viável.

# Durante a busca, o algoritmo mantém uma solução parcial (ou um caminho parcial) e verifica se essa solução parcial
# pode ser completada para formar uma solução completa. Se a solução parcial não pode ser completada, o algoritmo volta
# atrás (backtrack) e tenta uma outra opção.

# O algoritmo de backtracking é amplamente utilizado em problemas de otimização, combinação e permutação,
# jogos (como Sudoku) e muitas outras áreas. Ele pode ser implementado em diferentes linguagens de programação e é uma
# técnica muito poderosa e flexível para encontrar soluções para problemas complexos.

def backtrack_subgrupos(n, subgrupo_atual=None, soma_atual=0, ultimo=1):
    if subgrupo_atual is None:
        subgrupo_atual = []

    # se é uma solução
    if soma_atual == n:
        print(subgrupo_atual)  # imprime o subgrupo

    # se não é uma solução
    elif soma_atual < n:
        for i in range(ultimo, n+1):  # explora as possibilidades
            subgrupo_atual.append(i)
            backtrack_subgrupos(n, subgrupo_atual, soma_atual+i, i)
            subgrupo_atual.pop()


num_pessoas = int(input())
print(f'Uma sessão com {num_pessoas} pessoas pode ter sua audiência nos seguintes subgrupos:')
backtrack_subgrupos(num_pessoas)
