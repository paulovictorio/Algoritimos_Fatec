n = int(input("Entre com um número inteiro maior que zero: "))
igual = 0
for i in range(1, n+1):
    if n % i == 0:
        igual += 1    
    else:
        continue

if igual == 2:
    print(f"O numero {n} é primo")
else:
    print(f"O número {n} não é primo")
