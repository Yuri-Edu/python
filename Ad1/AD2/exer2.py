def espelhamento(nome_arquivo):
    offset = []
    with open(nome_arquivo, 'r') as arquivo:
        pos = 0
        for linha in arquivo:
            offset.append(pos)
            pos += len(linha)

    with open(nome_arquivo, 'r') as arquivo:
        total_linhas = len(offset)
        for i in range(total_linhas):
            arquivo.seek(offset[i])
            linha = arquivo.readline().rstrip('\n')

            arquivo.seek(offset[total_linhas - i - 1])
            linha_invertida = arquivo.readline().rstrip('\n')

            if linha != linha_invertida:
                return False
            return True
            
nome_arquivo = 'exemplo.txt'
if espelhamento(nome_arquivo):
    print("O conteúdo do arquivo é igual quando lido de trás para frente.")
else:
    print("O conteúdo do arquivo é diferente quando lido de trás para frente.")
           
