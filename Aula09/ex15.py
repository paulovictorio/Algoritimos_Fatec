matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento da posição [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

simetrica = True
for i in range(3):
    for j in range(3):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print("A matriz digitada é simétrica.")
else:
    print("A matriz digitada não é simétrica.")