# Função alternativa para verificar se um número é primo
def eh_primo(n):
	if n <= 1:
		return False
	return all(n % i != 0 for i in range(2, n))


def listarPaes(n):
	pares = []
	if n % 2 == 0:
		print("Listagem de números pares até", n, ":")
		for i in range(0, n + 1, 2):
			pares.append(i)
			print(i, end=" ")
		print("Fim da listagem de números pares.")
		

def listarImpars(n):
    impares = []
    if n % 2 != 0:
        print("Listagem de números ímpares até", n, ":")
        for i in range(1, n + 1, 2):
            impares.append(i)
            print(i, end=" ")
        print("Fim da listagem de números ímpares.")
    return impares	

def listarPrimos(lista):
    print("Listagem de Primos:")
    primos = []
    for n in lista:
        if eh_primo(n):
            primos.append(n)
            print(n, end=" ")
    print("Fim da listagem de números primos.")

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
            return
        listarPaes(numero)
        impares = listarImpars(numero)
        listarPrimos(impares)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")

if __name__ == "__main__":
    main()
	

		

