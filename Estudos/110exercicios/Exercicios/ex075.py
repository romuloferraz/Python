nums = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os números: {nums}')
if nums.count(9) != 0:
    print(f'o número 9 apareceu {nums.count(9)} vezes')
if nums.count(3) != 0:
    print(f'O primeiro 3 foi digitado na posição {nums.index(3)}')
print(f'O números pares são: ', end='')
for c in nums:
    if c % 2 == 0:
        print(f'{c} ', end='')
