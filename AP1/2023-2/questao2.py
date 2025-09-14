def eh_palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return eh_palindromo(s[1:-1])

def main():
    while True:
        s = input("Digite uma string (vazio para sair): ")
        if s == "":  # string vazia encerra o programa
            break
        if eh_palindromo(s):
            print(s)

# Executar o programa
main()


def test_eh_palindromo(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return test_eh_palindromo(s[1:-1])

def main_test():
    while True:
        s = input("Digite uma string: ")
        if s == "":  # string vazia encerra o programa
            break
        if test_eh_palindromo(s):
            print(s)

main_test()
        