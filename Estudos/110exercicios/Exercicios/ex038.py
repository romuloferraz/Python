n1 = int(input('Digite o primeiro número:\n'))
n2 = int(input('Digite o segundo número:\n'))
if n1 > n2:
    print(f'{n1} é o maior número')
elif n2 > n1:
    print(f'{n2} é o maior número')
else:
    print('O dois números são iguais')
