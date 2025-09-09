def criando(): 
    nomeAgenda = input("Digite o nome da agenda:")
    linhas = int(input("Digite a quantidade e linhas:"))

    telefone = int(input("Digite um telefone"))
    dados = open(nomeAgenda,"w")
    
    for i in range(linhas):
        nova = input("linha" + str(i+1) + ":")
        dados.write(nova + "\n")
    dados.close 

def inserindo(): 
    nome = input("Digite o nome do arquivo:")
    arquivo = open(nome, "a")
    telefone = int(input("digite o numero de telefone:"))

    arquivo.append(telefone + "\n")

    arquivo.close()

def lendo():
    nome = input("Digite o nome do arquivo:")
    dados = open(nome, 'r')
    linhas = dados.readlines()
    for linha in linhas:
            print(linha, end="")
    dados.close

nomeAgenda = criando()
telefone = criando()
print(lendo())      
   