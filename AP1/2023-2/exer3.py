import sys

# (a) Função que aplica a função de Collatz apenas uma vez


def collatz_uma_vez(n):
    if isinstance(n, int):  # Verifica se o valor é um número inteiro
        if n % 2 == 0:       # Se for par
            return n // 2    # Divide por 2
        else:                # Se for ímpar
            return 3 * n + 1  # Aplica a fórmula 3n + 1
    else:
        return f"Valor {n} não é inteiro"

# (b) Função que gera a sequência de Collatz até chegar no ciclo 4, 2, 1


def sequencia_collatz(n):
    if not isinstance(n, int):  # Verifica se a entrada é um número inteiro
        return f"Valor {n} não é inteiro"

    sequencia = [n]  # Começa a sequência com o número inicial
    while n != 1:  # Continua aplicando Collatz até chegar em 1
        if n % 2 == 0:  # Se for par
            n = n // 2
        else:           # Se for ímpar
            n = 3 * n + 1
        sequencia.append(n)  # Adiciona o novo valor à sequência
    return sequencia

# (c) Função que gera e imprime as sequências de Collatz para todos os inteiros de 3 até n


def sequencias_de_3_ate_n(n):
    if not isinstance(n, int):  # Verifica se é inteiro
        print(f"Valor {n} não é inteiro")
        return

    for i in range(3, n + 1):  # Para cada número de 3 até n
        seq = sequencia_collatz(i)  # Gera a sequência de Collatz
        print(f"Sequência de Collatz para {i}: {seq}")  # Exibe a sequência

# Função principal do programa


def main():
    # Solicita a entrada do usuário
    entrada = input("Digite um valor inteiro: ")

    try:
        valor = int(entrada)  # Tenta converter a entrada para inteiro
    except ValueError:
        # Mensagem de erro se não for inteiro
        print(f"Valor {entrada} não é inteiro")
        return  # Sai do programa

    # (a) Aplicação única da função de Collatz
    resultado = collatz_uma_vez(valor)
    print(f"\nResultado de Collatz aplicado uma vez: {resultado}")

    # (b) Sequência completa de Collatz
    print("\nSequência de Collatz completa:")
    sequencia = sequencia_collatz(valor)
    print(sequencia)

    # (c) Sequências de Collatz de todos os inteiros de 3 até valor
    print(f"\nSequência de Collatz de todos os números de 3 até {valor}:")
    sequencias_de_3_ate_n(valor)

    print("\nObrigado por utilizar nosso sistema!")  # Mensagem de encerramento


# Garante que a função main só seja executada se este script for o principal
if __name__ == "__main__":
    main()
