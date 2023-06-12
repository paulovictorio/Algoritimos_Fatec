matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = (int(input(f"Digite o numero {i+1},{j+1}: ")))
        linha.append(elemento)
    matriz.append(linha)

elemento_maior = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > elemento_maior:
            elemento_maior = elemento

matriz_resul = []
for linha in matriz:
    linha_resul = []
    for elemento in linha:
        elemento_resul = elemento * elemento_maior
        linha_resul.append(elemento_resul)
    matriz_resul.append(linha_resul)

for i in range(2):
    for j in range(2):
        print(f"{matriz_resul[i][j]}", end=" ")
    print()
