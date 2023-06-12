while True:
    num = int(input("Digite um numero: "))
    if num > 0:
        break
    print("Valor inválido. O valor deve ser 0 ou maior")

if (num == 0) or (num == 1):
    fatorial = 1
else:
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i

print(f"O valor de {num}! é igual a {fatorial}")