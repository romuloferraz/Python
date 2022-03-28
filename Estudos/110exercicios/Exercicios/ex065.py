resp = 's'
cont = soma = 0
list = []
while resp == 's':
    num = int(input('digite um número: '))
    cont += 1
    soma += num
    list.append(num)
    resp = input('Deseja continuar? [s/n]').lower().strip()
print(f'Você digitou {cont} números\n'
      f'A média deles é {soma/cont}\n'
      f'O maior  número é o {max(list)}\n'
      f'O menor número é o {min(list)}\n')
