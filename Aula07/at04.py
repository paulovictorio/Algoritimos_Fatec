lista = []
while True:
    num = int(input("Digite um número par: "))
    if num == 0:
        break
    if num % 2 == True:
        lista.append(num)
print(f"A média ariutimética dos pares é {sum(lista)/len(lista)}")

