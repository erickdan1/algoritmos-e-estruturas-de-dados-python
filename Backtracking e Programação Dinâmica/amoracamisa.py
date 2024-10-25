
def torcedores_fotografados(n, torcedores):
    if n == 0:
        return 0

    elif n == 1:
        return torcedores[0]

    soma = [0] * n
    soma[0] = torcedores[0]
    soma[1] = max(torcedores[0], torcedores[1])

    # cálculo da soma do numero de torcedores
    for i in range(2, n):
        soma[i] = max(soma[i - 1], soma[i - 2] + torcedores[i])

    return soma[-1]


num_setores = int(input())  # número de setores do estádio
qnt_torcedores = [int(i) for i in input().split()]  # quantidade de torcedores em cada setor

num_fotografados = torcedores_fotografados(num_setores, qnt_torcedores)

print(f'{num_fotografados} torcedores podem ser fotografados.')
