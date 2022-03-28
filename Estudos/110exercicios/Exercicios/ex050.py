s = 0
for c in range(0, 6):
    num = int(input(f'{c+1})Digite um número: '))
    if num % 2 == 0:
        s = s + num
print('='*40)
print(f'A soma de todos os pares digitados é: {s}')
