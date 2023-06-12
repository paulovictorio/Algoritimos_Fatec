nasc = int(input("Entre com seu ano de nascimento: "))
ano = int(input("Entre com o ano atual: "))
idade = ano - nasc
if idade >= 18:
    print(f"Você tem {idade}. Já pode tirar carteira de habilitação e votar!!")
elif idade < 16:
    print(f"Você tem {idade}. Não pode votar nem tirar carteira de habilitação")
else:
    print(f"Você tem {idade}. Já pode votar mas não pode tirar carteira de habilitação")