# Função que verifica se um número é primo
def primo(n):
    # Números menores que 2 não são primos (por definição matemática)
    if n < 2:
        return False

    # Verifica se algum número de 2 até a raiz quadrada de n divide n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Se dividir exato, não é primo
            return False

    # Se nenhum número dividiu, então é primo
    return True
