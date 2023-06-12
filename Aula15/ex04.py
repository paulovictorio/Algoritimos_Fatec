def verificar_ip(ip):
    end_ip = ip.split('.')
    if len(end_ip) != 4:
        return False
    for i in end_ip:
        try:
            if int(i) < 0 or int(i) > 255:
                return False
        except ValueError:
            return False
    return True

with open('aula15/entrada.txt', 'r') as arquivo:
    corretos, incorretos = [], []
    for i in arquivo:
        if verificar_ip(i.strip()):
            corretos.append(i)
        else:
            incorretos.append(i)

with open('aula15/saida.txt', 'w', encoding='utf-8') as saida:
    saida.write('[Endereços válidos:]\n')
    saida.writelines(corretos)
    saida.write('\n[Endereços inválidos:]\n')
    saida.writelines(incorretos)