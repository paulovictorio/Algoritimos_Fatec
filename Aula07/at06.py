n = int(input("Entre com um número: "))
fact = 1

if (n == 0) or (n == 1):
    fact = 1
else:
    fact = 1
    for i in range(1, n+1):
        fact *= i

print(f"O valor de {n} fatorial é {fact}")