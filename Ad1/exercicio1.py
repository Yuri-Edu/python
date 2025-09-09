def verificarDna(s):
    # Converter a string para maiúsculas
    s = s.upper()
    # Verifica se todos os caracteres pertencem ao conjunto válido de DNA (A, C, G, T)
    valido = all(c in "ACGT" for c in s)

    if valido:
        # verifica se uma sequência de DNA é válida e conta a ocorrência de cada base na sequência
        contagem = {"A": s.count("A"), "C": s.count(
            "C"), "G": s.count("G"), "T": s.count("T")}
        print("Sequência válida. Além disso, a contagem de cada base nitrogenada é:")
        for base, qtd in contagem.items():
            print(f"{base}: {qtd}")
    else:
        posicoes_invalidas = [i + 1 for i,
                              c in enumerate(s) if c not in "ACGT"]
        print(
            f"Sequência inválida, pois nas posições {posicoes_invalidas} os elementos não possuem valores esperados.")


def complemento_reverso(s):
    s = s.upper()
    if not all(c in "ACGT" for c in s):
        posicoes_invalidas = [i + 1 for i,
                              c in enumerate(s) if c not in "ACGT"]
        print(
            f"Sequência inválida, pois nas posições {posicoes_invalidas} os elementos não possuem valores esperados.")
        return

    complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverso_complementar = "".join(complemento[c] for c in reversed(s))

    print(f"Sequência original: {s}")
    print(f"Complemento reverso: {reverso_complementar}")


if __name__ == "__main__":
    s = input("Digite uma sequência de DNA: ")
    verificarDna(s)
    complemento_reverso(s)
