numeros = []
resp = 'S'
cont = 0
while resp not in 'nN':
    num = int(input('Insira um valor na lista: '))
    if cont == 0:
        numeros.append(num)
        print(f'Valor {num} inserido na posição 0')
    else:
        for j, k in enumerate(numeros):
            if num < k:
                numeros.insert(j, num)
                print(f'Valor {num} inserido na posição {j}')
                break
            elif num > numeros[-1] or cont == 0:
                numeros.append(num)
                print(f'O valor {num} foi inserido na última posição')
                break
    cont += 1
    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
print(numeros[::-1])
print(f'Você inseriu ao todo {cont} números.')
if 5 in numeros:
    print(f'O número 5 está na posição {numeros.index(5)}')
else:
    print('O número 5 não está na lista')



