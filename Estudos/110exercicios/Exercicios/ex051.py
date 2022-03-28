n0 = int(input('Digite o primeiro termo da PA: '))
p = int(input('digite o passo da PA: '))
for c in range(0, 10):
    print(f'{n0 + p*c} -> ', end='')
print('ACABOU')
