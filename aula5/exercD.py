# Função que decide o vencedor com base na escolha PAR ou IMPAR
def decidir(jogador1, escolha1, jogador2, escolha2, n, m):
    soma = n + m  # Soma dos números escolhidos pelos jogadores

    # Se a soma for PAR e o jogador1 escolheu PAR, ele vence
    # Se a soma for ÍMPAR e o jogador1 escolheu ÍMPAR, ele vence
    if (soma % 2 == 0 and escolha1 == "PAR") or (soma % 2 == 1 and escolha1 == "IMPAR"):
        return jogador1  # Jogador1 vence
    else:
        return jogador2  # Caso contrário, jogador2 vence


# Leitura do número de testes
QT = int(input())  # Número de rodadas do jogo

for _ in range(QT):  # Executa o jogo QT vezes
    # Lendo os nomes e escolhas dos jogadores em uma única linha
    entrada = input().split()
    jogador1, escolha1, jogador2, escolha2 = entrada[0], entrada[1], entrada[2], entrada[3]

    # Lendo os números escolhidos pelos jogadores
    n, m = map(int, input().split())

    # Determinando e imprimindo o vencedor
    print(decidir(jogador1, escolha1, jogador2, escolha2, n, m))
