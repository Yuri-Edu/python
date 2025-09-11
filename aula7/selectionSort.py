def selectionSort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

lista = [64, 25, 12, 22, 11]
print(selectionSort(lista))  # Deve retornar [11, 12, 22, 25, 64]