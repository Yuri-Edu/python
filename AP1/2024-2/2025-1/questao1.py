def mostrar_lista(entrada):
    entrada = entrada.split()
    separador = ' '
    return separador.join(entrada)

def compararLista(entrada):
    entrada = entrada.split()
    lista = []
    for i in range(len(entrada)-1):
        for j in range(i+1, len(entrada)):
            if entrada[i] == entrada[j]:
                lista.append(entrada[j])
    return lista

def repeticao(entrada):
    entrada = str(entrada).split()
    saida = []
    for i in entrada:
        if entrada.count(i) > 1 and i not in saida:
            saida.append(i)
            print(f"Números que se repetem: {mostrar_lista(' '.join(saida))}")
            print(f"O número {i} se repete {entrada.count(i)} vezes na lista.")
                
            

def main():
    entrada = input("Digite uma lista de números separados por espaço: ")
    print(f"Lista digitada: {mostrar_lista(entrada)}")
    repeticao(entrada)

if __name__ == "__main__":
    main() 
            
                