valores = []
for i in range(0,5):
    valores.append(int(input(f'Digite o {i+1}° valor: ')))
print(valores)
max = max(valores)
print(f'Maior valor: {max}')
print('Posições: ', end='')
for i, j in enumerate(valores):
    if j == max:
        print(f'{i}...', end='')
min = min(valores)
print(f'\nMenor valor: {min}')
print('Posições: ', end='')
for i, j in enumerate(valores):
    if j == min:
        print(f'{i}...', end='')

