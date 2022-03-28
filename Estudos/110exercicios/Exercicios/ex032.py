from datetime import date
ano = int(input('Digite o ano para analisar ou digite 0 para o ano atual:\n'))
if ano == 0:
    ano = date.today().year
if (ano % 100 != 0) and (ano % 4 == 0):
    print(f'{ano} é um ano bissexto!')
elif (ano % 100 == 0) and (ano % 400 == 0):
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissesxto!')
