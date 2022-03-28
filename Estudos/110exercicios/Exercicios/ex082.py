numeros = []
pares = []
impares = []
resp = 'S'
while resp not in 'nN':
    num = int(input('Insira um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = input('Deseja continuar? [S/N] ').upper().strip()
print(f'Todos: {numeros}\n'
      f'Pares: {pares}\n'
      f'Ímpares: {impares}')
