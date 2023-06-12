nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = nota1 + nota2 + nota3 /3

if media >=7.0:
    print(f"Aprovado")
if media >=3.0 <7.0:
    print(f"Exame")
if media ==0.0 <3.0:
    print(f"Reprovado")