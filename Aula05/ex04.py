h = float(input("Entre com a sua altura (m): "))
sexo = input("Qual o seu sexo? (M) ou (F) ")
if sexo.upper() == "F":
    peso = (62.1*h)-44.7
    print(f"Seu peso ideal é {peso: .1f} kg")
if sexo.upper() == "M":
    peso = (72.7*h)-58
    print(f"Seu peso ideal é {peso: .1f} kg")
else:
    print("Entre com um sexo válido")