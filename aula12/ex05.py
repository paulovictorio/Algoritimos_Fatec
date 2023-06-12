def volume(raio):
    r3 = raio ** 3
    volume = 4/3 * r3
    print(f"O volume da esfera é {volume:.2f}")


raioes = float(input("Entre com o raio da esfera: "))
volume(raioes)