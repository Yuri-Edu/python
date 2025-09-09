# programa que verifica se o tamanho de um texto é menor ou igual a 80 caracteres
# Se o tamanho do texto for menor ou igual a 80, imprime "YES", caso contrário, imprime "NO"
texto = input("Escreva um texto: ")

if len(texto) <= 80:
    print("YES")
else:
    print("NO")
