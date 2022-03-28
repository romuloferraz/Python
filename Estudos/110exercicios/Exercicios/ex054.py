from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input(f'{c+1})Digite o ano de nascimento: '))
    if (date.today().year - ano) > 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} acima de 18 anos\n'
      f'{menor} abaixo de 18 anos')
