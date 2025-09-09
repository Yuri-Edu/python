#def ler_aruivo(nome_arquivo):
 #  matriz = []
  # with open(nome_arquivo, 'r') as arquivo:
   #   for linha in arquivo:
    #     numeros = list(map(int, linha.strip().split()))
  #       matriz.append(numeros)
  #    return matriz
  # def obter_vizinos(matriz, i, j):
  #      vizinhos = []
  #      linhas = len(matriz)
  #      colunas = len(matriz[0])
  #      deslocamentos = [(-1, -1), (-1, 0), (-1, 1),
  #                   (0, -1),           (0, 1),
  #                   (1, -1),  (1, 0),  (1, 1)]
  #      for dx, dy in deslocamentos:
  #          ni, nj = i + dx, j + dy
  #          if 0 <= ni < linhas and 0 <= nj < colunas:
  #              vizinhos.append(matriz[ni][nj])
  #      return vizinhos
  # def encontrar_minimo(matriz):
  #      minimos = []
  #      linhas = len(matriz)
  #      colunas = len(matriz[0])
  #      for i in range(linhas):
  #          for j in range(colunas):
  #              valor = matriz[i][j]
  #              vizinhos = obter_vizinos(matriz, i, j)
  #              if all(valor < vizinho for vizinho in vizinhos):
  #                  minimos.append((i, j, valor))
  #      return minimos
  # def main():
  #     nome_arquivo = 'matriz.txt'
  #     matriz = ler_aruivo(nome_arquivo)
  #     minimos = encontrar_minimo(matriz)
  #     print("Valores mínimos locais encontrados:")
  #     for i, j, valor in minimos:
  #            print(f"Posição: ({i}, {j}), Valor: {valor}")
  #  if __name__ == "__main__":
  #      main()

# Função que lê a matriz de um arquivo texto
def ler_matriz(nome_arquivo):
    matriz = []  # Cria uma lista vazia para guardar a matriz

    # Abre o arquivo no modo leitura
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.strip():  # Verifica se a linha não está vazia
                # Quebra a linha em partes (números separados por espaço)
                # e converte cada um para inteiro
                numeros = list(map(int, linha.strip().split()))
                # Adiciona essa linha (como lista) dentro da matriz
                matriz.append(numeros)
    
    return matriz  # Retorna a matriz completa lida do arquivo


# Função que retorna uma lista com os vizinhos de uma posição da matriz
def vizinhos(matriz, linha, coluna):
    linhas = len(matriz)      # Número total de linhas na matriz
    colunas = len(matriz[0])  # Número total de colunas (assumindo matriz retangular)
    viz = []  # Lista que irá armazenar os valores dos vizinhos

    # Percorre as posições vizinhas (linha-1 até linha+1 e coluna-1 até coluna+1)
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            # Verifica se a posição (i, j) está dentro dos limites da matriz
            if 0 <= i < linhas and 0 <= j < colunas:
                # Verifica se (i, j) não é a própria célula
                if i != linha or j != coluna:
                    # Adiciona o valor do vizinho à lista
                    viz.append(matriz[i][j])

    return viz  # Retorna a lista de vizinhos


# Função que verifica cada célula da matriz
# e imprime se ela é menor que todos os seus vizinhos
def encontrar_celulas(matriz):
    linhas = len(matriz)      # Número total de linhas
    colunas = len(matriz[0])  # Número total de colunas

    # Percorre cada posição da matriz
    for i in range(linhas):
        for j in range(colunas):
            valor = matriz[i][j]              # Pega o valor da célula atual
            viz = vizinhos(matriz, i, j)      # Busca os vizinhos da célula

            # Verifica se TODOS os vizinhos são maiores que o valor da célula atual
            if all(v > valor for v in viz):
                # Se for verdade, imprime a posição (linha, coluna) e o valor
                print(f"Linha {i+1}, Coluna {j+1}, Valor = {valor}")
                # Observação: usamos i+1 e j+1 porque as linhas e colunas começam em 1 para o usuário


# Função principal que controla o fluxo do programa
def main():
    # Lê o nome do arquivo digitado pelo usuário
    nome_arquivo = input().strip()

    # Lê a matriz a partir do arquivo
    matriz = ler_matriz(nome_arquivo)

    # Chama a função para encontrar e imprimir as células que atendem à condição
    encontrar_celulas(matriz)


# Comando que executa o programa se for rodado diretamente
if __name__ == "__main__":
    main()
