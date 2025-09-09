# Passo 1: Criar vetor com os 61 primeiros termos de Fibonacci
fibonacci = [0, 1]  # já temos Fib(0) e Fib(1)

for i in range(2, 61):
    # Fib(n) = Fib(n-1) + Fib(n-2)
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# Passo 2: Ler número de casos de teste
T = int(input())

# Passo 3: Ler os casos de teste e imprimir o resultado
for _ in range(T):
    # Lê o índice n
    n = int(input())
    # Imprime o n-ésimo termo de Fibonacci
    print(f"Fib({n}) = {fibonacci[n]}")