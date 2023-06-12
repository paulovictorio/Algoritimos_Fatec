n1 = int(input("Entre com primeiro número: "))
n2 = int(input("Entre com segundo número: "))
acao = input("Qual operação deseja realizar? (media, diferenca, produto, divisao) ")

if acao.upper() == "MEDIA":
    result = (n1 + n2) / 2
    print(f"A media entre {n1} e {n2} é {result}")
elif acao.upper() == "DIFERENCA":
    if n1 > n2:
        result = n1 - n2
        print(f"A diferença entre os numeros {n1} e {n2} é {result}")
    elif n2 > n1:
        result = n2 - n1
        print(f"A diferença entre os números {n1} e {n2} é {result}")
elif acao.upper() == "PRODUTO":
    result = n1 * n2
    print(f"O produto entre os números {n1} e {n2} é {result}")
elif acao.upper() == "DIVISAO":
    result = n1 / n2
    print(f"O resultado da divisão entre {n1} e {n2} é {result}")
else:
    print(f"Operação inválida!!")