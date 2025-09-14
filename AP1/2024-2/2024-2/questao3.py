def criar_matriz_pessoas(nomes):
    matriz = []
    soma_idades = 0

    for nome in nomes:
        idade = int(input(f"Digite a idade de {nome}: "))
        profissao = input(f"Digite a profissão de {nome}: ")
        estado_civil = input(f"Digite o estado civil de {nome}: ")
        matriz.append([nome, idade, profissao, estado_civil])
        soma_idades += idade

        media_idade = soma_idades / len(nomes)
    return matriz, media_idade

def main():
    try:
        quantidade = int(input("Quantas pessoas você deseja inserir? "))
        if quantidade <= 0:
            print("Por favor, insira um número inteiro positivo.")
            return
        nomes = []
        for _ in range(quantidade):
            nome = input("Digite o nome da pessoa: ")
            nomes.append(nome)
        matriz, media_idade = criar_matriz_pessoas(nomes)
        print("\nMatriz de Pessoas:")
        for pessoa in matriz:
            print(pessoa)
        print(f"\nMédia de Idade: {media_idade:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
