print('=' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
cont = 2
print('1', end='')
while cont <= termos:
    n3 = n2 + n1
    print(f', {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1



