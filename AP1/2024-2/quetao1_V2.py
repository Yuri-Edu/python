def Ler_numeros():
    numeros = []
    while True:
        entrada = input()
        if entrada == "":
            break
        numeros.append(int(entrada))
    return numeros

def pares(lista):
    return [x for x in lista if x % 2 == 0]

def impares(lista):
    return [x for x in lista if x % 2 != 0]

def eh_primo(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, n))

def primos(lista):
    return [x for x in lista if eh_primo(x)]

def main():
    print("Digite números inteiros (uma linha em branco para terminar):")
    numeros = Ler_numeros()
    
    lista_pares = pares(numeros)
    lista_impares = impares(numeros)
    lista_primos = primos(lista_impares)
    
    print("Números pares:", lista_pares)
    print("Números ímpares:", lista_impares)
    print("Números primos (da lista de ímpares):", lista_primos)

if __name__ == "__main__":
    main()
