def moda(lista):
    auxiliar = [0] * len(lista)
    for i in range(len(lista)):
        auxiliar[i] = 1
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                auxiliar[i] += 1

    onde_mais_repetido = 0
    for i in range(len(auxiliar)):
        if auxiliar[i] > auxiliar[onde_mais_repetido]:
            onde_mais_repetido = i  
    return lista[onde_mais_repetido]

lista = [1, 2, 3, 4, 5, 1, 2, 1]
print(moda(lista))  # Deve retornar 1

def moda_com_dict(lista):
    frequencias = {}
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    mais_repetido = max(frequencias, key=frequencias.get)
    return mais_repetido

lista2 = [2, 3, 4, 2, 5, 3, 2] 
print(moda_com_dict(lista2))  # Deve retornar 2

def moda_com_collections(lista3):
    from collections import Counter
    contador = Counter(lista3)
    mais_repetido = contador.most_common(1)[0][0]
    return mais_repetido

lista3 = [5, 6, 5, 7, 8, 5, 6]
print(moda_com_collections(lista3))  # Deve retornar 5

def moda_com_statistics(lista4):
    from statistics import mode
    return mode(lista4)

lista4 = [9, 10, 9, 11, 12, 9]
print(moda_com_statistics(lista4))  # Deve retornar 9

def moda_com_statistics_multimodal(lista5):
    from statistics import multimode
    modas = multimode(lista5)
    return modas

lista5 = [1, 2, 2, 3, 3, 4]
print(moda_com_statistics_multimodal(lista5))  # Deve retornar [2, 3]

