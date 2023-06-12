gas = input("Digite o tipo de combustivel (a = Álcool/ d = Diesel/ g = Gasolina): ").upper
lit = int(input("Digite a quantidade de litros: "))
valor = 0
if gas == "A":
    valor = lit * 1.7997
    print(f"O preço sera de R${valor}")
elif gas == "D":
    valor = lit * 0.9798
    print(f"O preço sera de R${valor}")
elif gas == "G":
    valor = lit * 2.1009
    print(f"O preço sera de R${valor}")


