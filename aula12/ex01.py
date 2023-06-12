def imp(n):
    if n % 2 == 0:
        return True
    else: return False
#


e = int(input("Digite um número: "))
if imp(e):
    print(f"O número {e} é par")
else: print(f"O número {e} é impar")