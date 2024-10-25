def verifica(receba):
    contagem = 0  # Inicia a contagem verificadora em 0
    pilha = []  # Lista de posições de Fs
    posi = 0  # Contador de posição, opcional dependendo de como você implementa o loop
    for i in receba:  # Passa por cada caractere da entrada, sem precisar transformar em lista
        if contagem < 0:  # Se a contagem verificadora for para -1, significa V extra
            return posi
        if i == "F":
            contagem += 1  # F adiciona 1 a contagem verificadora
            posi += 1
            pilha.append(posi)
        elif i == "V":
            contagem -= 1  # V diminui 1 da contagem verificadora
            posi += 1
            if pilha:
                pilha = pilha[1:]  # Retira a posição do primeiro F da lista, pois ele foi “resolvido”
            else:
                return posi  # Redundância com o primeiro if! Pra mostrar como pode ser feito de maneiras diferentes
    if contagem != 0:  # Se no final da leitura da string contagem não for 0, sobraram Fs.
        return pilha[0]  # Retorna primeira posição da lista de posições de F
    else:  # Se for 0, a pilha está correta
        return -1


def main():
    receba = input()
    posicao = verifica(receba)  # Manda o input para a função e recebe a posição inválida (-1 em caso correto)

    if posicao != -1:
        print(f"Incorreto, devido a capa na posição {posicao}.")
    else:
        print("Correto.")


if __name__ == '__main__':
    main()
