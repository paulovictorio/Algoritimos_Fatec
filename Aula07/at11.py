while True:
    soma = 0
    m = int(input("Digite um número positivo: "))
    n = int(input("Digite um número positivo menor que o anterior: "))
    if m < 0 or n < 0:
        print("Os números devem ser positivos!")
    elif n >= m:
        print("O valor N deve ser inferior a M!")
    else:
        for i in range(n, m+1):
            soma += i
    print(f"A soma de (incluindo) {m} e {n} é {soma}")