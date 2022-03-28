palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('A', 'E', 'I', 'O', 'U')
for palavra in palavras:
    print(f'{palavra :.<30}', end='')
    print('Vogais: ', end='')
    for vogal in vogais:
        if vogal in palavra:
            print(f'{vogal} ', end='')
    print('')
