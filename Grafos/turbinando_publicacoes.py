
def busca_largura(graph, no):
    busca = []
    # marca todos os vértices como não visitados.
    visitados = [False] * (len(graph))

    # cria uma fila vazia para o BFS
    fila = [no]

    visitados[no] = True

    # enquanto a fila não for vazia
    while fila:

        # retira o último vértice inserido na fila e imprime
        no = fila.pop(0)
        busca.append(no)

        # Obtenha todos os vértices adjacentes dos vértices desenfileirados. Se um adjacente não foi visitado, marque-o
        # como visitado e coloque-o na fila
        for el in graph[no]:
            if visitados[el] is False:
                fila.append(el)
                visitados[el] = True

    return busca


def custo_boost(qnt_seg_pretendida):
    return qnt_seg_pretendida * 5.25


n = int(input())  # número de usuários na rede social
u = int(input())  # id do user
b = int(input())  # valor investido em boost

rede_social = []  # representação implícita

for i in range(n):
    seguidores = input().split()
    rede_social += [[int(i) for i in seguidores[2:]]]

seguidores_alcancados = []

boost = False

if b >= 15:
    boost = True

if boost:
    alcance = int(b // 5.25)
    seg = busca_largura(rede_social, u)
    seguidores_alcancados += seg[1:len(rede_social[u])+alcance+1]
    print([str(i) for i in seguidores_alcancados])

else:
    seguidores_alcancados += rede_social[u]
    print([str(i) for i in seguidores_alcancados])
