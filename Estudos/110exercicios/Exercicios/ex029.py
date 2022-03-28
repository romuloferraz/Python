vel = int(input('Velocidade do carro (KM/h): '))
m = 7*(vel-80)
if vel > 80:
    print('VOCÊ FOI MULTADO!!!\n'
          f'E Sua multa é de R${m}.')
else:
    print(f'Ok! Você está abaixo da máxima velocidade permitida!')
