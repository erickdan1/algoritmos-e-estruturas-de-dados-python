
visitados = []


def busca_profundidade(visitado, grafo, no):
    if no not in visitado:
        visitado.append(no)
        for vizinho in grafo[no]:
            busca_profundidade(visitado, grafo, vizinho)


n, m = [int(i) for i in input().split()]

rede_social = {}

for i in range(1, n+1):
    rede_social[i] = []

for i in range(m):
    conexoes = [int(i) for i in input().split()]
    rede_social.get(conexoes[0]).append(conexoes[1])
    rede_social.get(conexoes[1]).append(conexoes[0])

output = []

for i in rede_social.keys():
    busca_profundidade(visitados, rede_social, i)
    output.append(len(visitados))
    visitados.clear()

print(" ".join(map(str, output)))
