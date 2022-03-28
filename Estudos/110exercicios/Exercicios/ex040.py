n1 = float(input('NOTA 1:\n'))
n2 = float(input('NOTA 2: \n'))
media = (n1 + n2)/2
if media >= 7:
    print(f'Com a média {media} o aluno está APROVADO!')
elif media < 5:
    print(f'Com a média {media} o aluno está REPROVADO!')
else:
    print(f'Com a média {media} o aluno está de RECUPERAÇÃO!')
