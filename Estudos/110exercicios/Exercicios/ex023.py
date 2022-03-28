num = int(input('Digite um número\n'))
m = num//1000
if m < 1:
      m = 0
c = (num - 1000*m)//100
if c < 1:
      c = 0
d = (num - 1000*m - 100*c)//10
if d < 1:
      d = 0
u = (num - 1000*m - 100*c - 10*d)



print(f'Analisando o número {num}:\n'
      f'Unidades: {u}\n'
      f'Dezenas: {d}\n'
      f'Centenas: {c}\n'
      f'Milhas: {m}\n')
