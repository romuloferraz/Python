import moeda

num = float(input('digite um número '))
print(f'Metade de {num} > {moeda.metade(num)}')
print(f'Dobro de {num} > {moeda.dobro(num)}')
print(f'{num} + 10 > {moeda.aumentar(num, 10)}')
print(f'{num} - 10 > {moeda.diminuir(num, 10)}')
