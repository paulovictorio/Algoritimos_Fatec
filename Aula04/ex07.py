deposito = float(input("Digíte o valor do depósito: "))
juros = float(input("Digíte a taxa de juros (%): "))
rendimen = deposito * (juros / 100)
valortotal = deposito + rendimen

print(f"O valor do rendimento é {rendimen} e o valor total depois do rendimento é {valortotal}")