vetorA = []
vetorB = []
for i in range(10):
    a = int(input(f"Digite o {i+1}° número: "))
    vetorA.append(a)
    
vetorB = list(vetorA)
vetorB.sort()
print(vetorA, vetorB)