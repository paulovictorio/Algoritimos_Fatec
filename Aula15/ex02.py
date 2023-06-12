votacao = []
while True:
    try:
        voto = int(input("""Qual o melhor Sistema Operacional para uso em servidores?
        1- Windows Server
        2- Unix
        3- Linux
        4- Netware
        5- Mac OS
        6- Outro
        0- Terminar votação
        """))
    except ValueError:
        print('Valor inválido!')
        continue
    if voto not in range(0, 7):
        print('Valor inválido!')
        continue
    if voto == 0:
        break
    votacao.append(voto)
    
t = len(votacao)
if t:
    print('Sistema Operacional\tVotos\t %')
    print(f'{"-"*20}\t{"-"*7}\t {"-"*3}')
    sos = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
    maior = 0

    for i in sos:
        votos_so = votacao.count(sos.index(i) + 1)
        frequencia = 100 * (votos_so / t)
        print(f'{i:20}\t{votos_so}\t {frequencia:2.1f}%')
        
        if votos_so > maior:
            maior = votos_so
            so = i

    print(f'{"-"*20}\t{"-"*7}\t {"-"*3}')
    print(f'{"Total":20}\t{len(votacao)}')

    print(f'\nO Sistema Operacional mais votado foi o {so}, com {maior} voto(s), correspondendo a {100 * (maior / t):.1f}% dos votos.')
else:
    print('Nenhum voto')
