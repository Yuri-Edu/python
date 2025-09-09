def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


numero = []

while True:
    entrada = input().strip()
    if entrada == '':
        break
    numero.append(int(entrada))

pares = []
impares = []
primos = []

for n in numero:

    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    elif primo(n):
        primos.append(n)

    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 != 0:
        impares.append(numero)
    elif primo(numero):
        primos.append(numero)

print("Listagem de números pares:")
for n in pares:
    print(n)
print("Fim da lista de pares:")

print("Listagem de números ímpares:")
for n in impares:
    print(n)
print("Fim da lista de ímpares:")

print("Listagem de números primos:")
for n in primos:
    print(n)
print("Fim da lista de primos:")
print("Obrigado por utilizar nosso sistema")
