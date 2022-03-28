numeros = []
resp = ' '
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    while resp not in 'nNsS':
        resp = input('Gostaria de continuar? [S/N] ').upper().strip()[0]
    if resp in 'nN':
        break
    resp = ' '
print('='*50)
print(f'Você digitou os números: {sorted(numeros)}')
