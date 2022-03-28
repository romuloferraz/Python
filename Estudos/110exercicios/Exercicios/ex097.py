def cabecalho(msg):
    quant = len(msg.strip()) + 4
    print('='*quant)
    print(f'{msg.strip().upper(): ^{quant}}')
    print(f'='*quant)
cabecalho('programa de estagio P&D')
cabecalho('Curso de Python do Guanabara')
cabecalho('App Reckonect')
