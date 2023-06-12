import math
e = 0
n = int(input("Digite um número inteiro positivo: "))
b = int(input("Digite o valor da base: "))
while i <=n:
    e = e + math.pow(b, i)
    i = i + i

    
for i in range(1, n+1):
    e = e + math.pow(2, i)
print(f"O valor de E = {e:.2f}")