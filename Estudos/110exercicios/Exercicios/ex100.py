import random

num = []
def sortear(lst):
    lst.clear()
    print(f'Sorteando 5 valores para a lista: ', end='')
    for i in range(0,5):
        lst.append(random.randint(1, 10))
        print(lst[i], end=' ')
def somar(lst):
    s = 0
    for i in lst:
        if i % 2 == 0:
            s += i
    print(f'\nSomando os valores pares de {lst}, temos {s}')
sortear(num)
somar(num)
