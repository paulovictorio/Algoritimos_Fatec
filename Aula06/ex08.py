import math

com = float(input("Entre com o comprimento da casa (em m): "))
lar = float(input("Entre com a largura da casa (em m): "))
tinta = float(input("Tamanho da lata de tinta em litros (1L, 3.5L ou 20L): "))
arealateral = (com * 2.80)* 2 
areafrente = (lar * 2.80)* 2 - 1.68
areaparede = (areafrente + arealateral)
if tinta == 1:
    quantidade = areaparede / 3
    latas = math.ceil(quantidade)
    print(f"Como sua area das suas paredes é {round(areaparede)}m² serão necessarias {latas} latas de tinta de 1 Litro para pinta-la") 
if tinta == 3.5:
    quantidade = areaparede / 3
    pintura = quantidade / 3.5
    latas = math.ceil(pintura)
    print(f"Como sua area das suas paredes é {round(areaparede)}m² serão necessarias {latas} latas de tinta de 3,5 Litros para pinta-la") 
if tinta == 20:
    quantidade = areaparede / 3
    pintura = quantidade / 20
    latas = math.ceil(pintura)
    print(f"Como sua area das suas paredes é {round(areaparede)}m² serão necessarias {latas} latas de tinta de 20 Litros para pinta-la") 
