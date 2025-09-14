def ler_limites():
        minimo, maximo = map(int, input("Digite os valores mínimo e máximo separados por espaço: ").split())
        return minimo, maximo

def ler_numeros():
    numeros = []
    while True:
        linha = input("Digite um número inteiro (ou pressione Enter para terminar): ")
        if linha == "":
            break
        for num in linha.split():
            numeros.append(int(num))
    return numeros

def classificar_numeros(numeros, minimo, maximo):
    menores = [n for n in numeros if n < minimo]
    intermediarios = [n for n in numeros if minimo <= n <= maximo]
    maiores = [n for n in numeros if n > maximo]
    return menores, intermediarios, maiores

def mostrar_resultados(menores, intermediarios, maiores, minimo, maximo):
    print(f"Números menores que {minimo:.1f}:")
    for n in menores:
        print(n)
    print(f"Numeros maiores que {maximo:.1f}:")
    for n in maiores:
        print(n)
    print(f"Números entre {minimo:.1f} e {maximo:.1f}:")
    for n in intermediarios:
        print(n)

def main():
    minimo, maximo = ler_limites()
    numeros = ler_numeros()
    menores, intermediarios, maiores = classificar_numeros(numeros, minimo, maximo)
    mostrar_resultados(menores, intermediarios, maiores, minimo, maximo)

if __name__ == "__main__":
    main()    