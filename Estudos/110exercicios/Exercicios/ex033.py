n1 = int(input('Digite o primeiro número:\n'))
n2 = int(input('Digite o segundo número:\n'))
n3 = int(input('Digite o terceiro número: \n'))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'{n1} > {n2} > {n3}')
    else:
        print(f'{n1} > {n3} > {n2}')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'{n2} > {n1} > {n3}')
    else:
        print(f'{n2} > {n3} > {n1}')
else:
    if n2 > n1:
        print(f'{n3} > {n2} > {n1}')
    else:
        print(f'{n3} > {n1} > {n2}')
