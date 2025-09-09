def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        linha = ""
        for j in range(3):
            valor = tabuleiro[i][j] if tabuleiro[i][j] != " " else "_"
            linha += valor + "|"
        print(linha[:-1])
    print()


def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
    for j in range(3):
        if all(tabuleiro[i][j] == jogador for i in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False


def verificar_empate(tabuleiro):
    return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))


def jogar_partida():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    exibir_tabuleiro(tabuleiro)

    while True:
        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            linha, coluna = divmod(jogada, 3)

            if jogada < 0 or jogada > 8:
                print("Posição inválida! Escolha de 1 a 9.")
                continue
            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já foi escolhida! Tente outra.")
                continue

            tabuleiro[linha][coluna] = jogador_atual
            exibir_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} venceu!\n")
                return jogador_atual
            elif verificar_empate(tabuleiro):
                print("Empate!\n")
                return "empate"

            jogador_atual = "O" if jogador_atual == "X" else "X"

        except ValueError:
            print("Entrada inválida! Digite um número de 1 a 9.")


def jogo_da_velha():
    placar = {"X": 0, "O": 0, "empates": 0, "partidas": 0}

    while True:
        vencedor = jogar_partida()
        placar["partidas"] += 1
        if vencedor in ["X", "O"]:
            placar[vencedor] += 1
        else:
            placar["empates"] += 1

        print("1Placar:")
        print(f"Partidas: {placar['partidas']}")
        print(f"Vitórias X: {placar['X']}")
        print(f"Vitórias O: {placar['O']}")
        print(f"Empates: {placar['empates']}\n")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            print("Encerrando o jogo. Obrigado por jogar!")
            break


if __name__ == "__main__":
    jogo_da_velha()
