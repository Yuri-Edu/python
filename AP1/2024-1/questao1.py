def mais_digitos_que_outros(linha):
    digitos = sum(1 for c in linha if c.isdigit())
    letras = len(linha) - digitos
    return digitos > letras

def main():
    n = int(input("Quantas linhas você deseja inserir? "))
    for _ in range(n):
        linha = input("Digite uma linha de texto: ")
        if mais_digitos_que_outros(linha):
            print(linha)

if __name__ == "__main__":
    main()
