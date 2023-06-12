l1 = [ ]
l2 = [ ]

for i in range(5):
    f1 = input(f"Digite o {i + 1}° numero da primeira lista: ")
    l1.append(f1)
    f2 = input(f"Digite a {i + 1}° numero da segunda lista: ")
    l2.append(f2)
uniao = set(l1).union(l2)
print(f"a união das listas é {uniao}")
