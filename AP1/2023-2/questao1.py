def ciclos_permutacao(perm):
    n = len(perm)
    visitados = [False] * n
    ciclos = []

    for i in range(n):
        if not visitados[i]:
            ciclo = []
            atual = i
            while not visitados[atual]:
                ciclo.append(atual + 1)      # +1 para representar posição
                visitados[atual] = True
                atual = perm[atual] - 1      # -1 para ajustar índice
            ciclos.append(ciclo)

    return ciclos, len(ciclos)

# Testes
entrada1 = [7, 3, 2, 1, 5, 4, 6, 8, 15, 11, 10, 9, 13, 12, 14]
entrada2 = [1, 12, 10, 8, 6, 5, 7, 4, 9, 3, 11, 2, 13]

print(ciclos_permutacao(entrada1))
print(ciclos_permutacao(entrada2))
