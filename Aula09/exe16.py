matriz = [[int(input(f'Digite um elemento (linha {i+1}, coluna {j+1}): ')) for j in range(5)] for i in range(5)]
soma = 0
n = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i % 2 == 0:
            soma += matriz[i][j]
            n += 1

media = soma / n
print(f"A média dos elementos nas linhas pares é {media:.1f}")