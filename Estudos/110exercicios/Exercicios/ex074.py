import random

sorteio = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
print('Os números sorteados foram: ', end='')
for n in sorteio:
    print(f'{n} ', end='')
print(f'\nMaior: {max(sorteio)}')
print(f'Menor: {min(sorteio)}')
