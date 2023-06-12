frase = input("Digite uma frase: ")
qtd = 0
for letra in frase:
    if letra.lower() in 'aeiouáãâàéèêíìîóòõôúùûäëïöü':
        qtd += 1
print(f"Quantidade de vogais = {qtd}")
