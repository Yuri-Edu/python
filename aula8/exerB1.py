# Função que verifica se cada quadra é segura ('S') ou insegura ('U')
def verificar_seguranca(matriz):
    linhas = len(matriz)              # Número de linhas da matriz
    colunas = len(matriz[0])          # Número de colunas (assumimos que todas as linhas têm o mesmo número de colunas)
    resultado = []                    # Lista que vai armazenar as linhas da saída final (compostas por 'S' e 'U')

    # Percorre cada linha da matriz
    for i in range(linhas):
        linha_resultado = ''          # String que vai guardar o resultado da linha atual

        # Percorre cada coluna (célula) da linha atual
        for j in range(colunas):

            # Se o valor da célula for 1, ela é insegura
            if matriz[i][j] == 1:
                linha_resultado += 'U'

            else:
                inseguro = False       # Assumimos que a célula é segura, até provar o contrário

                # Verificamos os vizinhos diretos: cima, baixo, esquerda e direita
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + dx, j + dy  # Calcula a posição do vizinho

                    # Verifica se o vizinho está dentro da matriz
                    if 0 <= ni < linhas and 0 <= nj < colunas:

                        # Se o vizinho for perigoso (1), a célula se torna insegura
                        if matriz[ni][nj] == 1:
                            inseguro = True
                            break     # Não precisa verificar os outros vizinhos

                # Se for insegura por causa do vizinho, marca 'U', senão marca 'S'
                linha_resultado += 'U' if inseguro else 'S'

        # Adiciona a linha processada na lista de resultado
        resultado.append(linha_resultado)

    return resultado  # Retorna todas as linhas processadas ('S' e 'U')


# --- Início da leitura da entrada ---

# Lê o número de linhas que devem ser exibidas na saída
N = int(input())

matriz = []  # Lista para armazenar a matriz completa
# Lê N + 1 linhas da matriz, como mostrado nos exemplos
for _ in range(N + 1):
    linha = list(map(int, input().split()))  # Converte a linha de entrada em uma lista de inteiros
    matriz.append(linha)                     # Adiciona a linha à matriz

# Processa a matriz e obtém o resultado com 'S' e 'U'
saida = verificar_seguranca(matriz)

# Imprime apenas as N primeiras linhas do resultado, como pedido
for i in range(N):
    print(saida[i])