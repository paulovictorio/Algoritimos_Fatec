mediap = 0
mediaa = 0
imc = []
for i in range (1, 6):
    peso = int(input(f"Digite o {i}° peso em KG: "))
    altura = float(input(f"Figite a {i}° altura em metros: "))
    mediap = peso
    mediaa = altura
    imc.append(peso/(altura*2))
print(f"A média de pesos é {mediap/20}kg")
print(f"A média de altura é {mediaa/20} metros")
print(f"E o maior e menor imc são {max(imc)} e {min(imc)}")
