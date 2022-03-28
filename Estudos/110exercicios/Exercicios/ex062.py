print('Gerador de Pa')
print('=' * 20)
num1 = int(input('Digite o primeiro termo da PA: '))
p = int(input('Digite o passo da PA: '))
n = 1
termos = 10
while 2 % 2 == 0:
    while n <= termos:
        print(f'{num1*n} >> ', end = '')
        n += 1
    print('PAUSA!')
    termos = termos + int(input('Quantos termos você quer mostrar a mais? '))
