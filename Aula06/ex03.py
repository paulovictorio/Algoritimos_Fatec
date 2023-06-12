n = float(input("Entre com o valor do produto: "))
if n <= 1000:
    valor = n - n * 0.1
    desconto = n * 0.1
    print(f"Com um desconto de 10% seu produto ficou R${valor}, sendo descontado R${desconto} do preço dele")
if n > 1000 and n <= 5000:
    valor = n - n * 0.2
    desconto = n * 0.2
    print(f"Com um desconto de 20% seu produto ficou ${valor}, sendo descontado R${desconto} do preço dele")
if n > 5000:
    valor = n - n * 0.3
    desconto = n * 0.3
    print(f"Com um desconto de 30% seu produto ficou ${valor}, sendo descontado R${desconto} do preço dele")