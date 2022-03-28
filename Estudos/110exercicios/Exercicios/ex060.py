num = int(input('Digite o número para descobrir o fatorial:\n'))
print('Calculando...\n'
      f'{num}! = ', end = '')
fat = num
while num > 1:
    print(f'{num} x ', end = '')
    num -= 1
    fat = fat * num
print(f'1 = {fat}')
