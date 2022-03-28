import statistics
n1 = float(input('Nota 1\n'))
n2 = float(input('Nota 2\n'))
media = statistics.fmean([n1, n2])
print(f'A média do aluno foi {media:.2f}')



