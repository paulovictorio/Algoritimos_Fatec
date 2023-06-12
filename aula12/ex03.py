def bissexto(n):
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

n = int(input("Digite um ano: "))
if bissexto(n):
    print(f"Esse ano é bissexto")
else:
    print(f"Esse anos não bissexto")