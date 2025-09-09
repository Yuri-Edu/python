# Função para ler e exibir o conteúdo do arquivo
def ler_e_mostrar_conteudo(nome_arquivo):
    print(f"\nConteúdo do Arquivo {nome_arquivo}:")
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            print(linha.strip()) 

# Função para encontrar a palavra de maior comprimento e suas linhas
def encontrar_maior_palavra(nome_arquivo):
    maior_palavra = ""  # Armazena a maior palavra encontrada
    linhas_ocorrencia = []  # Lista das linhas onde ela aparece

    with open(nome_arquivo, 'r') as arquivo:
        numero_linha = 1  # Contador de linhas começando em 1
        for linha in arquivo:
            palavras = linha.strip().split()  # Separa as palavras da linha
            for palavra in palavras:
                if len(palavra) > len(maior_palavra):
                    # Nova palavra maior encontrada
                    maior_palavra = palavra
                    linhas_ocorrencia = [numero_linha]  # Reinicia a lista de linhas
                elif len(palavra) == len(maior_palavra):
                    # Palavra com mesmo tamanho da maior
                    if numero_linha not in linhas_ocorrencia:
                        linhas_ocorrencia.append(numero_linha)
            numero_linha += 1  # Incrementa o número da linha

    return maior_palavra, linhas_ocorrencia

# Função principal que processa o arquivo
def processar_arquivo(nome_arquivo):
    ler_e_mostrar_conteudo(nome_arquivo)  # Exibe o conteúdo do arquivo
    maior_palavra, linhas = encontrar_maior_palavra(nome_arquivo)  # Encontra a maior palavra
    print(f"\nPalavra de Maior Comprimento: {maior_palavra}")  # Mostra a palavra
    linhas_str = ' '.join(map(str, linhas))  # Converte lista de números em string
    print(f"Qual(is) Linha(s) Ocorreu: {linhas_str}")  # Mostra as linhas onde ela aparece

# Lista dos arquivos para testar
arquivos = ['Drummond.txt', 'pensamento.txt']

# Processa cada arquivo da lista
for arquivo in arquivos:
    processar_arquivo(arquivo)
