numeros = []
cont = 0
while cont < 5:
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

print(numeros)



