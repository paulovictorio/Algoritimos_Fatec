def MDC(a, b):
    while(b != 0):
        resto = a % b
        a = b
        b = resto
    return a

x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))
print(f"O MDC (maxímo divisor comum) de {x} e {y} é {MDC(x, y)}")