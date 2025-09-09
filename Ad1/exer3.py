def verificarDna(s):
    s = s.upper()

    valido = all(c in "ACGT" for c in s)

    if valido:
        contagem = {"A": s.count("A"), "C": s.count(
            "C"), "G": s.count("G"), "T": s.count("T")}
        print("Sequência válida. Além disso, a contagem de cada base nitrogenada é:")

        for base, qtd in contagem.items():
            print(f"{base}: {qtd}")

        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        reversoComplementar = "".join(complemento[c] for c in reversed(s))
        print(
            f"Dada a sequência {s}, seu reverso complementar é: {reversoComplementar}")
    else:
        posicoesInvalidas = [i + 1 for i, c in enumerate(s) if c not in "ACGT"]
        print(
            f"Sequência inválida, pois nas posições {posicoesInvalidas} os elementos não possuem valores esperados.")


teste = input("Digite uma sequência de DNA: ")
verificarDna(teste)
