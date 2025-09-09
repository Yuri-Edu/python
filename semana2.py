import random

palpites = 0
numero = random.randint(1, 100)

while True:
    chute = int(input("Digite um número entre 1 e 100: "))
    palpites += 1

    if chute < numero:
        print("Muito baixo! Tente novamente.")
    elif chute > numero:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero} em {palpites} tentativas.")
        break
    