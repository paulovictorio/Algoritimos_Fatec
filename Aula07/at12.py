soma = 0
pessoas = 0

while True:
    idade = int(input("Digite a idade (ou 0 para sair): "))
    
    if idade == 0:
        break
    
    soma += idade
    pessoas += 1

if pessoas > 0:
    media = soma / pessoas
    print(f"A idade média é {media}")
    print(f"O número total de pessoas é {pessoas}")
else:
    print("Nenhuma idade foi inserida")