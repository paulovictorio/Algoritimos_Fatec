numero = input("Digite um número inteiro positivo: ")

if not numero.isdigit() or int(numero) <= 0:
    print("Número inválido!")
else:
    numero = int(numero)
    numero_invertido = int(str(numero)[::-1])
    print("Número invertido:", numero_invertido)
