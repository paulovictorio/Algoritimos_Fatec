from funcoes import roladado

dadojogador = 0
dadonpc = 0
press = 'S'
while press == 'S':
    dadojogador = roladado()
    dadonpc = roladado()

    print(dadojogador)
    print(dadonpc)

    if dadojogador > dadonpc:
        print("Você venceu")

    elif dadojogador == dadonpc:
        print("Empate")

    else:
        print("Você perdeu")


    press = input("Digite a tecla S para dar outra rolada de dados ou enter para finalizar: ").upper().strip()
