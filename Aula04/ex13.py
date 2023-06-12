salario_minimo = float(input("Digite Seu Sálario Mínimo: "))
valor_kwatts = salario_minimo / 8
consumo = float(input("Consumo em Kwatts: "))
conta = valor_kwatts * consumo
conta_desconto = conta - (conta * 0.15)
print(f"Valor kwatts.................R$ {valor_kwatts:.2f}")
print(f"Valor da conta...............R$ {conta:.2f}")
print(f"Valor da conta com desconto: R$ {conta_desconto:.2f}")