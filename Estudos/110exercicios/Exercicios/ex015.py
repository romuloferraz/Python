dias = int(input('Quantos dias vocês alugou o carro?\n'))
dist = float(input('Quantos Km vc andou com o carro?\n'))
total = dias*60 + dist*0.15
print(f'O total a ser pago é de R${total}')
