import math

def eh_quadrado_perfeito(n):
    raiz = math.isqrt(n)
    if raiz * raiz == n:
        return f"{n} é quadrado perfeito"
    else:
        return f"{n} não é quadrado perfeito"

def listar_numeros(numeros):
    for numero in numeros:
        if numero % 3 == 0:
            print(f"{numero} é divisível por 3")
        elif numero % 5 == 0:
            print(f"{numero} é divisível por 5")
        else:
            print(eh_quadrado_perfeito(numero))

def main():
    try:
        entrada = input("Digite uma lista de números inteiros separados por vírgula: ")
        numeros = [int(num.strip()) for num in entrada.split(",")]
        listar_numeros(numeros)
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros separados por vírgula.")

if __name__ == "__main__":
    main()