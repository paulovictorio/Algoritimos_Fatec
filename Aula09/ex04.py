vetor = []
x = ""
for i in range(20):
    max = 10
    x = input(f"Digite a {i+1}ª palavra: ")
    saida = x[0:10]
    inverter = saida[::-1]
    vetor.append(inverter)
print(vetor)

