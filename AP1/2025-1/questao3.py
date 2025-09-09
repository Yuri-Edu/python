import random

def gerar_lista_aleatoria(tamanho):
    vetor = [random.random() for _ in range(tamanho)]
    return vetor

def mostrar_lista(entrada):
      for valor in entrada:
        print(f"{valor:.2f}", end=" ")
        
def BubbleSort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

def main():
    tamanho = int(input("Digite o tamanho da lista: "))
    lista_aleatoria = gerar_lista_aleatoria(tamanho)
    print("Lista gerada:")
    mostrar_lista(lista_aleatoria)
    print()
    lista_ordenada = BubbleSort(lista_aleatoria)
    print("Lista ordenada:")
    mostrar_lista(lista_ordenada)



if __name__ == "__main__":
    main()