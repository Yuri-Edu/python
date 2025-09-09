def verificarDna(s, k, n):
    s = s.upper()

    valido = all(c in "ACGT" for c in s)

    if valido:
        contagem = {"A": s.count("A"), "C": s.count(
            "C"), "G": s.count("G"), "T": s.count("T")}
        print("Sequência válida. Além disso, a contagem de cada base nitrogenada é:")

        for base, qtd in contagem.items():
            print(f"{base}: {qtd}")

        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        reverso_complementar = "".join(complemento[c] for c in reversed(s))
        print(
            f"Dada a sequência {s}, seu reverso complementar é: {reverso_complementar}")

        if k > len(s):
            print("Valor de k maior que o tamanho da sequência.")
        else:
            substrings = {}
            for i in range(len(s) - k + 1):
                sub = s[i:i+k]
                substrings[sub] = substrings.get(sub, 0) + 1

            substrings_repetidas = [sub for sub,
                                    count in substrings.items() if count >= n]

            if substrings_repetidas:
                print("Substrings que aparecem ao menos", n, "vezes:")
                for sub in substrings_repetidas:
                    print(sub)
            else:
                print("Nenhuma substring de tamanho", k,
                      "aparece pelo menos", n, "vezes.")
    else:
        posicoesInvalidas = [i + 1 for i, c in enumerate(s) if c not in "ACGT"]
        print(
            f"Sequência inválida, pois nas posições {posicoesInvalidas} os elementos não possuem valores esperados.")


testek = int(input("Digite o valor de k: "))
testen = int(input("Digite o valor de n: "))
testes = input("Digite uma sequência de DNA: ")
verificarDna(testes, testek, testen)
