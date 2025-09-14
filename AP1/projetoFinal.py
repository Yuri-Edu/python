import random
from collections import Counter

# ---------- PARTE 1: CADASTRO DE PESSOAS ----------
def cadastrar_pessoas():
    nomes_str = input("Digite os nomes das pessoas (separados por vírgula): ")
    nomes = [n.strip() for n in nomes_str.split(",")]
    matriz = []
    idades = []

    for nome in nomes:
        idade = int(input(f"Idade de {nome}: "))
        profissao = input(f"Profissão de {nome}: ")
        estado_civil = input(f"Estado civil de {nome}: ")
        matriz.append([idade, profissao, estado_civil, nome])
        idades.append(idade)

    media = sum(idades) / len(idades)
    print(f"\nMédia das idades: {media:.2f}\n")

    return matriz


# ---------- PARTE 2: CLASSIFICAÇÃO NUMÉRICA ----------
def ler_limites_e_numeros():
    minimo, maximo = map(float, input("Digite os limites mínimo e máximo: ").split())
    numeros = []
    print("Digite os números (linha vazia para encerrar):")
    while True:
        entrada = input()
        if entrada == "":
            break
        for v in entrada.split():
            numeros.append(float(v))
    return minimo, maximo, numeros


def classificar_numeros(numeros, minimo, maximo):
    menores = [x for x in numeros if x < minimo]
    meio = [x for x in numeros if minimo <= x < maximo]
    maiores = [x for x in numeros if x >= maximo]
    return menores, meio, maiores


# ---------- PARTE 3: ESTATÍSTICA ----------
def calcular_moda(numeros):
    if not numeros:
        return None
    contagem = Counter(numeros)
    return contagem.most_common(1)[0][0]


def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


# ---------- PARTE 4: FILTROS EXTRAS ----------
def pares(numeros):
    return [n for n in numeros if n % 2 == 0]

def impares(numeros):
    return [n for n in numeros if n % 2 != 0]

def eh_primo(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def primos(numeros):
    return [n for n in numeros if eh_primo(int(n))]


# ---------- PARTE 5: FRASES ----------
def inverter_frase(frase):
    return " ".join(frase.split()[::-1])


# ---------- MAIN ----------
def main():
    print("===== CADASTRO DE PESSOAS =====")
    pessoas = cadastrar_pessoas()

    print("\n===== CLASSIFICAÇÃO NUMÉRICA =====")
    minimo, maximo, numeros = ler_limites_e_numeros()
    menores, meio, maiores = classificar_numeros(numeros, minimo, maximo)
    print(f"\nMenores que {minimo}: {menores}")
    print(f"Entre {minimo} e {maximo}: {meio}")
    print(f"Maiores ou iguais a {maximo}: {maiores}")

    print("\n===== ESTATÍSTICA =====")
    print("Moda:", calcular_moda(numeros))
    print("Ordenado com Bubble Sort:", bubble_sort(numeros[:]))

    print("\n===== FILTROS =====")
    print("Pares:", pares(numeros))
    print("Ímpares:", impares(numeros))
    print("Primos:", primos(numeros))

    print("\n===== FRASES =====")
    frase = input("Digite uma frase: ")
    print("Frase invertida:", inverter_frase(frase))

    print("\nObrigado por utilizar nosso sistema!!!")


if __name__ == "__main__":
    main()
