lista = []
for i in range(5):
    x = int(input("Digite um valor: "))
    lista.append(x)
t = tuple(lista)
print(t[::-1])