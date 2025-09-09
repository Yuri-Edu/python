def ler_arquivo(nome_arquivo):
    vendas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # Remove quebras de linha
            if linha:  # Ignora linhas vazias
                data, produto, quantidade, preco = linha.split(',')
                vendas.append({
                    'data': data,
                    'produto': produto,
                    'quantidade': int(quantidade),
                    'preco': float(preco)
                })
    return vendas


def faturamento_por_data(vendas):
    total_por_data = {}
    for venda in vendas:
        data = venda['data']
        total = venda['quantidade'] * venda['preco']
        if data in total_por_data:
            total_por_data[data] += total
        else:
            total_por_data[data] = total

    print('\nFaturamento por data:')
    for data in sorted(total_por_data):
        print(f'{data}: R$ {total_por_data[data]:.2f}')


def faturamento_por_produto(vendas):
    total_por_produto = {}
    for venda in vendas:
        produto = venda['produto']
        total = venda['quantidade'] * venda['preco']
        if produto in total_por_produto:
            total_por_produto[produto] += total
        else:
            total_por_produto[produto] = total

    print('\nFaturamento por produto:')
    for produto in sorted(total_por_produto):
        print(f'{produto}: R$ {total_por_produto[produto]:.2f}')


# --- Programa principal ---

vendas = ler_arquivo('vendas.txt')

while True:
    print("\nMenu:")
    print("1 - Mostrar faturamento por data")
    print("2 - Mostrar faturamento por produto")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        faturamento_por_data(vendas)
    elif opcao == '2':
        faturamento_por_produto(vendas)
    elif opcao == '3':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
