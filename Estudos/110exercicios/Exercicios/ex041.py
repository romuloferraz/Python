from datetime import date
ano = int(input('Digite o ano de nascimento do atleta:\n'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    clf = 'Mirim'
elif idade <= 14:
    clf = 'Infantil'
elif idade <= 19:
    clf = 'Júnior'
elif idade <= 25:
    clf = 'Sênior'
else:
    clf = 'Master'
print(f'O atleta tem {idade} anos\n'
          f'Classificação: {clf}')
