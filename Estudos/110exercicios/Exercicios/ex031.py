dist = float(input('Qual a distância da viagem (Km)?\n'))
if dist > 200:
    preco = dist*0.45
else:
    preco = dist*0.5
print('='*40)
print(f'O valor da viagem ficou em R$ {preco}')
print('='*40)

