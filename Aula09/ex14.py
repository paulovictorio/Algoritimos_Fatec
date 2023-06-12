matriz = [[int(input(f'Digite um elemento (linha {i+1}, coluna {j+1}): ')) for j in range(10)] for i in range(10)]
vetor = []

for i in range(len(matriz[0])):
    soma = 0
    for n in range(len(matriz)):
        soma += matriz[n][i]
    vetor.append(soma)

resultado = [sum(x * y for x, y in zip(row, vetor)) for row in matriz]

print("A matriz multiplicada pelo vetor com as somas das linhas:")
for row in resultado:
    print(row)
