def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.readlines()
    return [linha.strip() for linha in conteudo]

def contar_ocorrencias(lista):
    contagem = {}
    for linha in lista:
        palavras = linha.lower().split()
        for palavra in palavras:
            palavra = palavra.strip('.,!?;:"()[]{}')  # Remove pontuação
            if palavra:
                contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def mostrar_ocorrencias(contagem):
    print("Contagem de palavras (em ordem decrescente):")
    palavras_ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
    for palavra, frequencia in palavras_ordenadas:
        print(f"{palavra}: {frequencia}")

# Programa principal
nome_arquivo = 'exemplo.txt'
conteudo = ler_arquivo(nome_arquivo)
contagem = contar_ocorrencias(conteudo)
mostrar_ocorrencias(contagem)
