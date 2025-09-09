# Função que lê e exibe o conteúdo do arquivo na tela
def ler_e_mostrar_conteudo(nome_arquivo):
    print(f"\nConteúdo em {nome_arquivo}:")  # Exibe o nome do arquivo
    with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo em modo leitura
        for linha in arquivo:  # Percorre cada linha do arquivo
            print(linha.strip())  # Remove quebras de linha e espaços extras e exibe

# Função que calcula a média de todos os números no arquivo
def calcular_media(nome_arquivo):
    soma = 0  # Acumulador para a soma dos números
    contador = 0  # Contador para a quantidade de números

    with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo em modo leitura
        for linha in arquivo:  # Percorre cada linha do arquivo
            numeros = map(float, linha.strip().split())  
            # Separa os números da linha, converte para float
            
            for numero in numeros:  # Para cada número na linha
                soma += numero  # Soma os números
                contador += 1   # Conta a quantidade de números

    if contador == 0:  # Evita divisão por zero, caso o arquivo estivesse vazio
        return 0
    return soma / contador  # Retorna a média

# Função que conta quantos números estão acima da média
def contar_acima_da_media(nome_arquivo, media):
    contador = 0  # Contador de números acima da média

    with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo em modo leitura
        for linha in arquivo:  # Percorre cada linha do arquivo
            numeros = map(float, linha.strip().split())  
            # Separa os números da linha, converte para float

            for numero in numeros:  # Para cada número na linha
                if numero > media:  # Se o número for maior que a média
                    contador += 1   # Incrementa o contador

    return contador  # Retorna o total de números acima da média

# Função principal que processa o arquivo
def processar_arquivo(nome_arquivo):
    ler_e_mostrar_conteudo(nome_arquivo)  # Mostra o conteúdo do arquivo
    media = calcular_media(nome_arquivo)  # Calcula a média dos números
    print(f"\nMédia dos Números em {nome_arquivo}: {media}")  # Exibe a média
    acima = contar_acima_da_media(nome_arquivo, media)  # Conta quantos estão acima da média
    print(f"Quantidade Acima de {media} em {nome_arquivo}: {acima}")  # Exibe a quantidade

# Lista dos arquivos que serão processados
arquivos = ['alfa.txt', 'beta.txt', 'gama.xyz']

# Percorre cada arquivo da lista e processa
for arquivo in arquivos:
    processar_arquivo(arquivo)
