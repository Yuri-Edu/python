x = []
# Leitura do vetor com 10 valores inteiros
for i in range(10):
    valor = int(input())

# Substituir valores nulos ou negativos por 1
    if valor <= 0:
        valor = 1

    x.append(valor)

    for i in range(10):
        print(f'X[{i}] = {x[i]}')
