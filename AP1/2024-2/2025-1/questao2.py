def inverter_frase(frase):
    frase = frase.split()
    frase_invertida = ' '.join(frase[::-1])
    return frase_invertida

def frase_separada(frase):
    frase = frase.split()
    separador = ','
    return separador.join(frase)

def data(data):
    data = data.split('/')
    print(data)
    data_formatada = '-'.join(data[::-1])
    print(f"Data no formato AAAA-MM-DD: {data_formatada}")

def main():
    frase = input("Digite uma frase: ")
    frase_invertida = inverter_frase(frase)
    print(f"Frase invertida: {frase_invertida}")
    print(f"Frase separada por vírgulas: {frase_separada(frase)}")
    data_input = input("Digite uma data no formato DD/MM/AAAA: ")
    data(data_input)
main()