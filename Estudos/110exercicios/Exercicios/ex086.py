Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('='*40)
print('GERADOR DE MATRIZ')
print('='*40)
for i in range(0, 3):
    for j in range(0, 3):
        Matriz[i][j] = int(input(f'Insira um valor na linha {i}, coluna {j}: '))
print( '='*40)
print('\n')
print(f"{'A = ': ^17}")
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{Matriz[i][j]: ^3}] ', end='')
    print('')
