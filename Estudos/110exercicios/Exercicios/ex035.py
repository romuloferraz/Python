a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))
n1 = False
n2 = False
n3 = False
if (a < b + c) and (a > abs(b - c)):
    n1 = True
if (b < a + c) and (b > abs(a - c)):
    n2 = True
if (c < a + b) and (c > abs(a - b)):
    n3 = True
if (n1 and n2 and n3):
    print(f'{a}, {b}, {c} conseguem formar um triângulo')
else:
    print(f'{a}, {b}, {c} não conseguem formar um triângulo')
