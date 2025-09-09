def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.readlines()
    print(f"Conteúdo original: {conteudo}")
    return [linha.strip() for linha in conteudo]

def inverter_arquivo(lista):
    lista_invertida = lista[::-1]
    print(f"Conteúdo invertido: {lista_invertida}")
    return lista_invertida

def escrever_arquivo(nome_arquivo, lista):
    with open(nome_arquivo, 'w') as arquivo:
        for linha in lista:
            arquivo.write(linha + '\n')
    print(f"Arquivo '{nome_arquivo}' atualizado com sucesso.")

# comando para executar o programa
nome_arquivo = 'exemplo.txt'
lista = ler_arquivo(nome_arquivo)
lista_invertida = inverter_arquivo(lista)
escrever_arquivo(nome_arquivo, lista_invertida)
