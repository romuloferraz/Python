import math
a = float(input('Valor do cateto oposto: '))
b = float(input('Valor do cateto adjacente: '))
h = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(f'A hipotenusa é {h}')
