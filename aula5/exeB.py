# criando um vetor vazio
x = []
# Laço que vai repetir 10 vezes (de i = 0 até 9)
for i in range(10):
    # Lê um número inteiro do usuário e armazena na variável valor
    valor = int(input("Digite um número: "))
    # Se o número for menor ou igual a 0, atribui 1 a valor
    if valor <= 0:
        valor = 1
    # Adicionamos o valor na lista X (já corrigido, se necessário)
    x.append(valor)
# Agora, mostramos todos os valores da lista com seus índices
for i in range(10):
    print(f"x[{i}] = {x[i]}")        