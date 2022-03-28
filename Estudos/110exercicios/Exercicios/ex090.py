aluno = {}
aluno['nome'] = input('Nome: ').capitalize().strip()
aluno['média'] = float(input('Média: '))
if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

