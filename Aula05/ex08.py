n = float(input("Entre com o preço do produto: "))
codigo = int(input("Entre com o Código de origem do produto: "))

if codigo == 1:
    preco = n + (n * 0.11)
    procedencia = "Sul"
    print(f"O valor final do produto com procedencia do {procedencia} é {preco}")
elif codigo == 2:
    preco = n + (n * 0.13)
    procedencia = "Norte"
    print(f"O valor final do produto com procedencia do {procedencia} é {preco}")
elif codigo == 3:
    preco = n + (n * 0.09)
    procedencia = "Nordeste"
    print(f"O valor final do produto com procedencia do {procedencia} é {preco}")
elif codigo == 4:
    preco = n + (n * 0.12)
    procedencia = "Centro-Oeste"
    print(f"O valor final do produto com procedencia do {procedencia} é {preco}")
elif codigo == 5:
    preco = n + (n * 0.18)
    procedencia = "Sudeste"
    print(f"O valor final do produto com procedencia do {procedencia} é {preco}")
else:
    print("Código inválido")
