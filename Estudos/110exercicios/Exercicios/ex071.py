valor = int(input('Qual valor você gostaria de sacar? R$ '))
cedulas_50 = valor//50
cedulas_20 = (valor - 50*cedulas_50)//20
cedulas_10 = (valor - 50*cedulas_50 - 20*cedulas_20)//10
cedulas_1 = (valor - 50*cedulas_50 - 20*cedulas_20 - 10*cedulas_10)
print(f'{cedulas_50} nota(s) de R$ 50')
print(f'{cedulas_20} nota(s) de R$ 20')
print(f'{cedulas_10} nota(s) de R$ 10')
print(f'{cedulas_1} nota(s) de R$ 1')

