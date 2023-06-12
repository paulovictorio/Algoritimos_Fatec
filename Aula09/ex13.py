maior = 0
linha = 0
coluna = 0

matriz = [[int(input(f'Digite um elemento (linha {i+1}, coluna {j+1}): ')) for j in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i + 1
            coluna = j + 1

print(f'O maior número é {maior} e está localizado na linha {linha} e coluna {coluna}')