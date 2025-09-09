def calcular_minutos(hora1, hora2):
    h1 = int(hora1[:2]) * 60 + int(hora1[3:])
    h2 = int(hora2[:2]) * 60 + int(hora2[3:])
    return h2 - h1

def converter_para_horas(minutos):
    horas = abs(minutos) // 60
    mins = abs(minutos) % 60
    return f"{horas}h {mins}min"

def analisar_ponto(arquivo):
    totais = {}  # código: [nome, minutos_trabalhados]

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(",")
            if len(partes) != 7:
                continue  # ignora linhas mal formatadas
            # atrbui a cada variavel uma parte da variavel partes fatiada pelo slipt
            cod, nome, data, entrada, saida_almoco, volta_almoco, saida = partes

            manha = calcular_minutos(entrada, saida_almoco)
            tarde = calcular_minutos(volta_almoco, saida)
            minutos_dia = manha + tarde

            if cod not in totais:
                totais[cod] = [nome, 0]
            totais[cod][1] += minutos_dia

    CARGA_ESPERADA = 160 * 60  # 160 horas em minutos

    for cod in sorted(totais):
        nome, minutos = totais[cod]
        diff = minutos - CARGA_ESPERADA

        if diff > 0:
            status = "✅ HORA EXTRA"
        elif diff < 0:
            status = "⚠️ DÉFICIT"
        else:
            status = "✔️ OK"

        horas_trabalhadas = converter_para_horas(minutos)
        diferenca = converter_para_horas(diff)
        print(f"{cod} - {nome}: {horas_trabalhadas} ({diferenca}) {status}")

# Chamada da função para processar o arquivo
analisar_ponto("pontos_0325.txt")
