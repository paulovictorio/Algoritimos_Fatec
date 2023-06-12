n = int(input("Digite o 1º valor: "))
m = int(input("Digite o 2º valor: "))
soma = n + m
if soma > 1000:
    print("A soma é maior que mil")
elif soma < 1000:
    print("A soma é menor que mil")
else:
    print("A some é mil")
print(soma)