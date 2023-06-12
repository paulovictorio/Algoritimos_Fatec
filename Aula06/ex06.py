q = int(input("Entre com o seu número de acertos na prova: "))
if q >= 0 and q < 50:
    print(f"Com {q} acertos sua nota foi D")
else:
    if q >= 50 and q < 70:
        print(f"Com {q} acertos sua nota foi C")
    else:
        if q >= 70 and q < 81:
            print(f"Com {q} acertos sua nota foi B")
        else:
            if q >= 80 and q < 101:
                print(f"Com {q} acertos sua nota foi A. Parabêns!!!")
            else:
                print("Quantidade de acertos inválida!")
        