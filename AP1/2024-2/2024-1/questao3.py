def langford(n):
    seq = [0] * (2 * n)
    resultados = []

    def colocar(numero):
        if numero == 0:  # todos os números foram colocados
            resultados.append(seq.copy())
            return

        for i in range(2 * n):
            j = i + numero + 1
            if j < 2 * n and seq[i] == 0 and seq[j] == 0:
                seq[i] = seq[j] = numero
                colocar(numero - 1)
                seq[i] = seq[j] = 0  # backtrack

    colocar(n)

    if resultados:
        for r in resultados:
            print(r)
        print(f"Há {len(resultados)} sequências")
    else:
        print(f"Não há sequências possíveis com o valor {n} de entrada")

# Exemplos de teste
langford(2)
langford(3)
langford(4)
