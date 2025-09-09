# Importa o módulo math para usar funções matemáticas como sqrt (raiz quadrada)
import math

# Função que lê 'qtd' pontos fornecidos pelo usuário


def ler_pontos(qtd):
    pontos = []  # Lista vazia para armazenar os pontos
    for _ in range(qtd):  # Loop que se repete 'qtd' vezes
        x = float(input("Digite x: "))  # Lê a coordenada x do ponto
        y = float(input("Digite y: "))  # Lê a coordenada y do ponto
        # Adiciona o ponto como uma tupla (x, y) na lista
        pontos.append((x, y))
    return pontos  # Retorna a lista de pontos lidos

# Função que verifica se um ponto está dentro (ou sobre a borda) de uma circunferência


def ponto_dentro(ponto, centro, raio):
    x1, y1 = ponto       # Coordenadas do ponto a ser verificado
    x2, y2 = centro       # Coordenadas do centro da circunferência
    # Calcula a distância entre o ponto e o centro da circunferência usando a fórmula da distância
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # Retorna True se a distância for menor ou igual ao raio (está dentro ou na borda)
    return distancia <= raio

# Função que recebe a lista de pontos e verifica para cada circunferência quais pontos estão dentro dela


def verificar_pontos(pontos):
    while True:  # Loop infinito que será interrompido com um break
        # Lê os dados da circunferência: centro (xC, yC) e raio (rC)
        xC = float(input("Digite x do centro da circunferência: "))
        yC = float(input("Digite y do centro da circunferência: "))
        rC = float(input("Digite o raio da circunferência: "))

        # Condição de parada: se todos os valores forem zero, encerramos o loop
        if xC == 0 and yC == 0 and rC == 0:
            break  # Encerra o loop

        centro = (xC, yC)  # Cria uma tupla com o centro da circunferência

        # Mensagem de início da listagem
        print("Pontos dentro da circunferência:")
        for ponto in pontos:  # Percorre todos os pontos fornecidos anteriormente
            # Verifica se o ponto está dentro da circunferência
            if ponto_dentro(ponto, centro, rC):
                print(f"{ponto}")  # Se estiver dentro, imprime o ponto

# Função principal que organiza o fluxo do programa


def main():
    # Lê a quantidade de pontos que o usuário deseja informar
    qtd = int(input("Quantos pontos deseja informar? "))
    pontos = ler_pontos(qtd)  # Chama a função para ler os pontos
    # Chama a função que verifica os pontos dentro das circunferências
    verificar_pontos(pontos)
    print("Obrigado por utilizar nosso sistema!!!")  # Mensagem final


# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Executa a função principal se o script for rodado diretamente
