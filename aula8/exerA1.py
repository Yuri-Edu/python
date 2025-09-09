n, m = map(int, input().split()) 
terreno = []

for _ in range(n):   # Um loop que roda n vezes (uma vez para cada linha do terreno).
    terreno.append(list(map(int, input().split())))  #Para cada linha:
achou = False

for i in range(1,n-1):
    for j in range(1, m-1):
        if terreno[i][j] == 42:
            if (terreno[i-1][j-1] == 7 and terreno[i-1][j] == 7 and terreno[i-1][j+1] == 7 and
                terreno[i][j-1] == 7 and terreno[i][j+1] == 7 and
                terreno[i+1][j-1] == 7 and terreno[i+1][j] == 7 and terreno[i+1][j+1] == 7):

                print(i+1, j+1)
                achou = True
            break
    if achou:
        break
if not achou:
    print("0 0")

