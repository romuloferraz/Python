from datetime import date
nasc = int(input('Digite seu ano de nascimento:\n'))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print('Esse é o ano de você se alistar!')
elif idade > 18:
    if (idade -18) == 1:
        print('Você já deveria ter se alistado há 1 ano\n'
              f'seu alistamento foi em {nasc + 18}')
    else:
        print(f'Você já deveria ter se alistado há {idade - 18} anos\n'
              f'seu alistamento foi em {nasc + 18}')
else:
    print(f'Faltam {18 - idade} anos para você se alistar!'
          f'Seu alistamento será em {nasc + 18}')
