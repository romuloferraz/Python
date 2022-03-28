import time
notas = []
cont = 0
while True:
    resp = ' '
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    cont += 1
    media = (nota1 + nota2)/2
    notas.append([cont, nome, nota1, nota2, media])
    while resp not in 'nNsS':
        resp = input('Quer continuar? [S/N] ').strip()
    if resp in 'nN':
        break
print('-='*20)
print(f"{'No. ': <4}{'NOME ': <16}{'MÉDIA ': >4}")
print('-'*30)
for i in range(0, cont):
    print(f"{notas[i][0]: <4}", end='')
    print(f"{notas[i][1]: <16}", end='')
    print(f"{notas[i][4]: >4}",)
time.sleep(1)
resp2 = input('Mostras notas de qual aluno? \n' )
for i in range(0, cont):
    if notas[i][1] == resp2:
        print(f'As notas de {notas[i][1]} são:\n'
              f'Nota 1: {notas[i][2]}\n'
              f'Nota 2: {notas[i][3]}')
