print('Gerador de Pa')
print('=' * 20)
num1 = int(input('Digite o primeiro termo da PA: '))
p = int(input('Digite o passo da PA: '))
n = 1
while n < 11:
    print(f'{num1*n} >> ', end = '')
    n += 1
print('FIM!')
