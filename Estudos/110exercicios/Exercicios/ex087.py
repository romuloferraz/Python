Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = 0
s3 = 0
l2 = []
print('='*40)
print('GERADOR DE MATRIZ')
print('='*40)
for i in range(0, 3):
    for j in range(0, 3):
        Matriz[i][j] = int(input(f'Insira um valor na linha {i}, coluna {j}: '))
        if Matriz[i][j] % 2 == 0:
            s += Matriz[i][j]
        if j == 2:
            s3 += Matriz[i][j]
        if i == 1:
            l2.append(Matriz[i][j])
print( '='*40)
print('\n')
print(f"{'A = ': ^17}")
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{Matriz[i][j]: ^3}] ', end='')
    print('')
print('='*40)
print(s, s3, max(l2))
