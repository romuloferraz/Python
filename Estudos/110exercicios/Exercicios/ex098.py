import time

def contagem(a, b, i):
    print(f'Contagem de {a} a {b} de {i} em {i}:')
    if i == 0:
        i = 1
    if a > b and i > 0:
        i = -i
        b = b - 1
    else:
        b = b + 1
    print('-='*15)
    print('=>',end=' ')
    for j in range(a, b, i):
        time.sleep(0.4)
        print(j, end=' ')
    print()

contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!\n')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
print('FIM!')


"""print('-='*15)
print('Contagem de 1 a 10 de 1 em 1:')
print('=>',end=' ')
for i in range(1, 11):
    time.sleep(0.4)
    print(i, end=' ')
print()
print('-='*15)
print('Contagem de 10 a 0 de 2 em 2:')
print('=>',end=' ')
for j in range(10, 0, -2):
    time.sleep(0.4)
    print(j, end=' ')"""
