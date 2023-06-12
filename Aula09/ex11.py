matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o elemento da posição [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("Matriz informada:")
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=" ")
    print()

soma_diagonal = 0
for i in range(4):
    soma_diagonal += matriz[i][i]

print(f"A soma dos elementos da diagonal principal é: {soma_diagonal}")