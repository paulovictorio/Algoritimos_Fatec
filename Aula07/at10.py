base = float(input("digite a vase do triângulo: "))
while base <= 0:
    base = float(input("Digite a base do triângulo > 0: "))

while True:
    altura = float(input("Digite a altura do triângulo"))
    if altura >= 0:
        break

area = (base * altura) / 2
print(area)