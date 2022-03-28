def cabecalho(msg):
    quant = len(msg.strip()) + 4
    print('\033[0:29:42m='*quant)
    print(f'{msg.strip().upper(): ^{quant}}')
    print(f'='*quant)
    print('\033[m', end='')
def ajuda():
    global resp
    resp = ''
    _help = input('\033[0:30:44mFunção ou Biblioteca > \033[m').strip().lower()
    if _help != 'fim':
        print('\033[0:35:40m')
        print(help(_help))
        print('\033[m')
    else:
        msg = 'ATÉ LOGO'
        quant = len(msg.strip()) + 4
        print('\033[0:29:41m~'*quant)
        print(f'{msg.strip().upper(): ^{quant}}')
        print(f'~'*quant)
        print('\033[m', end='')
        resp = 'fim'
cabecalho('SISTEMA DE AJUDA PyHELP')
while True:
    ajuda()
    if resp == 'fim':
        break

