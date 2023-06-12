def seg(h, m, s):
    return (h * 3600 + m * 60 + s)
#


hora = input("Digite a hora como hh:mm:ss: ")
h = hora.split(":")
seg = seg(int(h[0]), int(h[1]), int(h[2]))
print(f"O total é {seg} segundos")