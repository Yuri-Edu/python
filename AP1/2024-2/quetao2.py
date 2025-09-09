def ler_minimo(numero, minimo):
    print(f"Menores que {minimo}:")
    for i in numero:
        if i < minimo:
            print(i, end=" ")
    print("Fim da listagem de números menores que o mínimo.")
def listar_intermediarios(numeros, minimo, maximo):
    print(f"Números entre {minimo} e {maximo}:")
    for i in numeros:
        if minimo <= i <= maximo:
            print(i, end=" ")
    print("Fim da listagem de números intermediários.")

def ler_maximo(numero, maximo):
    print(f"Maiores que {maximo}:")
    for i in numero:
        if i > maximo:
            print(i, end=" ")
    print("Fim da listagem de números maiores que o máximo.")

def main():
    try:
        quantidade = int(input("Quantos números você deseja inserir? "))
        if quantidade <= 0:
            print("Por favor, insira um número inteiro positivo.")
            return
        numeros = []
        for _ in range(quantidade):
            num = int(input("Digite um número inteiro: "))
            numeros.append(num)
        minimo = int(input("Digite o valor mínimo: "))
        maximo = int(input("Digite o valor máximo: "))
        ler_minimo(numeros, minimo)
        listar_intermediarios(numeros, minimo, maximo)
        ler_maximo(numeros, maximo)
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros válidos.")    
    
if __name__ == "__main__":
        main()