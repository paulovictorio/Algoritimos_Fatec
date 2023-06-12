pontos = float(input("Digite a quantidade de pontos necessários (em mil unidades): "))
cotacao = float(input("Digite a cotação do dólar: "))
pontosdolar = 1.5
gastos = (pontos / pontosdolar) * cotacao

print(f"Você terá que gastar ${gastos:.2} para obter a quantidade de pontos desejada.")