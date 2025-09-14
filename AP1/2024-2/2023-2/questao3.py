def escada(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    a, b = 1, 2  # F(1), F(2)
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def main():
    n = int(input())
    formas = escada(n)
    print(f"Posso subir a escada de {n} degraus de")
    print(formas, "formas")

# Teste com 1000 degraus
# main()
