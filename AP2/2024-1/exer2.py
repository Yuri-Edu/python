# Função que lê os nomes do arquivo e retorna uma lista de nomes
def ler_nomes(nome_arquivo):
    nomes = []  # Lista para armazenar os nomes

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if linha.strip():  # Verifica se a linha não está vazia
                    nomes.append(linha.strip())  # Adiciona o nome (linha) à lista
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        exit()

    return nomes  # Retorna a lista de nomes


# Função que conta as ocorrências de primeiros nomes e sobrenomes
def contar_nomes(nomes):
    primeiros = {}  # Dicionário para os primeiros nomes
    ultimos = {}    # Dicionário para os sobrenomes (últimos nomes)

    for nome_completo in nomes:
        partes = nome_completo.split()  # Divide o nome completo em partes (separado por espaço)

        if len(partes) >= 1:
            primeiro = partes[0]          # Primeiro nome
            ultimo = partes[-1]           # Último nome (sobrenome)

            # Conta primeiro nome
            if primeiro in primeiros:
                primeiros[primeiro] += 1
            else:
                primeiros[primeiro] = 1

            # Conta sobrenome
            if ultimo in ultimos:
                ultimos[ultimo] += 1
            else:
                ultimos[ultimo] = 1

    return primeiros, ultimos  # Retorna dois dicionários


# Função que encontra os nomes mais frequentes (a moda)
def encontrar_moda(dicionario):
    if not dicionario:
        return []

    max_freq = max(dicionario.values())  # Maior frequência encontrada
    # Lista com todos os nomes que possuem a maior frequência
    moda = [nome for nome, freq in dicionario.items() if freq == max_freq]
    return moda


# Função principal que gerencia o programa
def main():
    nome_arquivo = input().strip()  # Lê o nome do arquivo

    nomes = ler_nomes(nome_arquivo)  # Lê os nomes do arquivo

    if not nomes:  # Verifica se a lista está vazia
        print("Arquivo Vazio!")
        return

    primeiros, ultimos = contar_nomes(nomes)  # Conta primeiros nomes e sobrenomes

    moda_primeiros = encontrar_moda(primeiros)  # Encontra a moda dos primeiros nomes
    moda_ultimos = encontrar_moda(ultimos)      # Encontra a moda dos sobrenomes

    # Imprime os resultados
    print("Nome(s) da Moda:")
    for nome in moda_primeiros:
        print(f"\t{nome}")

    print("Sobrenome(s) da Moda:")
    for sobrenome in moda_ultimos:
        print(f"\t{sobrenome}")


# Executa o programa
if __name__ == "__main__":
    main()
