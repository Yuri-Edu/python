import struct  # Para ler o arquivo binário
import re      # Para tratar o formato do CEP


# Função para carregar os fretes do arquivo binário
def carregar_fretes(arquivo_frete):
    fretes = {}
    try:
        with open(arquivo_frete, "rb") as f:
            while True:
                dados = f.read(16)  # 8 bytes para CEP + 8 bytes para o valor
                if not dados:
                    break  # Fim do arquivo
                cep, valor_frete = struct.unpack('8sd', dados)
                cep = cep.decode('utf-8')
                fretes[cep] = valor_frete
    except FileNotFoundError:
        print("Arquivo de frete não encontrado.")
        exit()
    return fretes


# Função para carregar os produtos do arquivo texto
def carregar_produtos(arquivo_produto):
    produtos = {}
    try:
        with open(arquivo_produto, "r") as f:
            for linha in f:
                partes = linha.strip().split()
                if len(partes) == 2:
                    loja = partes[0]
                    preco = float(partes[1])
                    produtos[loja] = preco
    except FileNotFoundError:
        print("Arquivo de produto não encontrado.")
        exit()
    return produtos


# Função para limpar o CEP (retirar pontos e traços)
def limpar_cep(cep):
    return re.sub(r'\D', '', cep).zfill(8)  # Remove não dígitos e garante 8 dígitos


# Função principal
def main():
    # Ler os nomes dos arquivos e o CEP
    nome_arquivo_frete = input("Digite o nome do arquivo de frete: ")
    nome_arquivo_produto = input("Digite o nome do arquivo de produto: ")
    cep_destino = input("Digite o CEP de destino: ")

    # Limpar o CEP (deixar só números com 8 dígitos)
    cep_destino = limpar_cep(cep_destino)

    # Carregar os dados
    fretes = carregar_fretes(nome_arquivo_frete)
    produtos = carregar_produtos(nome_arquivo_produto)

    # Verificar se o CEP existe no arquivo de frete
    if cep_destino not in fretes:
        print("O produto desejado não pode ser entregue neste frete.")
        return

    # Obter valor do frete para esse CEP
    valor_frete = fretes[cep_destino]

    # Calcular os preços totais (produto + frete) por loja
    menor_valor = None
    melhor_loja = None

    for loja, preco_produto in produtos.items():
        preco_total = preco_produto + valor_frete
        if menor_valor is None or preco_total < menor_valor:
            menor_valor = preco_total
            melhor_loja = loja

    # Exibir o resultado
    print(f"A melhor loja para o CEP {cep_destino} é {melhor_loja}, com valor total de R$ {menor_valor:.2f}.")


# Executar o programa
if __name__ == "__main__":
    main()
