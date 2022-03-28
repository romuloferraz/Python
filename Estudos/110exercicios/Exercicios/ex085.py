pares = []
impares = []
numeros = [pares, impares]

for i in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Pares: {sorted(numeros[0])}')
print(f'Ímpares: {sorted(numeros[1])}')
