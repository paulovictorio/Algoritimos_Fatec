def primo(n):
    resultado = False
    if n == 1: resultado
    elif (n==2 or n==3): resultado = True
    else:
        for i in range(2, n-1):
            if n % i == 0:
                resultado = False
                break
            else: resultado= True
    return resultado
#


numero = int(input("Digite um número: "))
if primo(numero):
    print(f"O numero {numero} é primo")
else: print(f"O número {numero} não é primo")
