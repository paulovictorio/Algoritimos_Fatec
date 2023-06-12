while True:
    nome_atleta = input("Digite o nome do atleta (ou deixe em branco para encerrar): ")

    if not nome_atleta:
        break

    saltos = [float(input(f"Digite a distância alcançada no {i}º salto: ")) for i in range(1, 6)]

    media_saltos = sum(saltos) / len(saltos)

    print("\nResultado final:")
    print("Atleta:", nome_atleta)
    print("Saltos:", " - ".join(map(str, saltos)))
    print("Média dos saltos:", media_saltos, "m\n")