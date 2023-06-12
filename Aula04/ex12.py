degrau = float(input("Entre com altura dos degraus em centímetros(cm): "))
altura = float(input("Entre com altura que você deseja alcançar em metros(m): "))

degraum = degrau / 100
degraus = altura / degraum
degraus = round(degraus)


print(f"Serão necessários {degraus} degraus para atingir {altura}m")
