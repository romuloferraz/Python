import random
import time
num = []

def analisar(lst):
    print('Analisando os valores passados', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.')
    for i in lst:
        print(f'{i} ', end='')
    print(f': Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {max(lst)}')
    num.clear()

def sorteio():
    cont = random.randint(1, 10)
    for i in range(0, cont):
        num.append(random.randint(0, 100))

for k in range(0, 5):
    sorteio()
    analisar(num)
