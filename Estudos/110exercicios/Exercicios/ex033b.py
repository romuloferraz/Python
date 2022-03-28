n1 = int(input('Digite o primeiro número:\n'))
p = n1
n2 = int(input('Digite o segundo número:\n'))
if n1 > n2:
    s = n2
else:
    p = n2
    s = n1
n3 = int(input('Digite o terceiro número: \n'))
if n3 > p:
    t = s
    s = p
    p = n3
elif n3 > s:
    t = s
    s = n3
else:
    t = n3
print(f'{p} > {s} > {t}')

