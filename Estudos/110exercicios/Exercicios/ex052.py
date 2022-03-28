num = int(input("Digite um número Natural: "))
#cont = 0
#list = []
list_div = []
for c in range(1, num + 1):
    if num % c == 0:
        #cont += 1
        list_div.append(c)
    #list.append(c)
print(list)
print('='*40)
print(f'{num} possui {len(list_div)} divisores!\n'
      f'Os dividores de {num} são: {list_div}')
if len(list_div) == 2:
    print(f'{num} é primo')
