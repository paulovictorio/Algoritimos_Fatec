a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))
if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Os lados formam um: ")
    if ((a == b) and (b == c)):
        print("Triangulo Equilátero")
    elif (a == c) or (b == c) or (a == c):
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os lados informados não formam um triângulo")