def abrir_arquivo(nome_arquivo):
    registros = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(',')
            if len(partes) != 7:
                continue
            codigo, nome, data, entrada, saida_almoco, volta_almoco, saida = partes
            registros.append({
                'codigo': codigo,
                'nome': nome,
                'data': data,
                'entrada': entrada,
                'saida_almoco': saida_almoco,
                'volta_almoco': volta_almoco,
                'saida': saida
            })
    return registros

def hora_para_minutos(hora_str):
    horas, minutos = map(int, hora_str.split(':'))
    return horas * 60 + minutos

def calcular_horas_trabalhados(registros):
    totais = {}
    for registro in registros:
        codigo = registro['codigo']
        entrada = hora_para_minutos(registro['entrada'])
        saida_almoco = hora_para_minutos(registro['saida_almoco'])
        volta_almoco = hora_para_minutos(registro['volta_almoco'])
        saida = hora_para_minutos(registro['saida'])

        horas_trabalhadas = (saida_almoco - entrada) + (saida - volta_almoco)

        if codigo not in totais:
            totais[codigo] = {
                'nome': registro['nome'],
                'horas_trabalhadas': 0
            }
        totais[codigo]['horas_trabalhadas'] += horas_trabalhadas
    return totais

def exibir_resultados(totais):
    for codigo, dados in totais.items():
        horas = dados['horas_trabalhadas']
        horas_str = f"{horas // 60}h {horas % 60}min"
        print(f"Código: {codigo}, Nome: {dados['nome']}, Horas Trabalhadas: {horas_str}")

abrir_arquivo('pontos_0325.txt')
registros = abrir_arquivo('pontos_0325.txt')
totais = calcular_horas_trabalhados(registros)
exibir_resultados(totais)      
    

