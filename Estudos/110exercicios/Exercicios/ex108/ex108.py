import moeda

num = float(input('digite um número '))
print(f'Metade de {moeda.moeda(num)} > {moeda.moeda(moeda.metade(num))}')
print(f'Dobro de {moeda.moeda(num)} > {moeda.moeda(moeda.dobro(num))}')
print(f'{moeda.moeda(num)} + R$ 10 > {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'{moeda.moeda(num)} - R$ 10 > {moeda.moeda(moeda.diminuir(num, 10))}')
