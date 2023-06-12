somapesos = 0
somaalturas = 0
maiorimc = 0
menorimc = 0

for i in range(1, 6):
    print(f"Digite os dados da {i}ª pessoa :")
    peso = float(input("Peso (em kg): "))
    altura = float(input("Altura (em metros): "))

    imc = peso / (altura ** 2)

    somapesos += peso
    somaalturas += altura
    maiorimc = max(maiorimc, imc)
    menorimc = min(menorimc, imc)

mediapeso = somapesos / 5
mediaalt = somaalturas / 5

print(f"O peso médio foi {mediapeso:.2f} kg, a altura média foi {mediaalt:.2f} metros, o maior IMC foi {maiorimc:.2f} e o menor IMC foi {menorimc:.2f}")
