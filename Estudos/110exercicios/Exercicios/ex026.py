nome = input('Digite aqui seu nome: ').strip().lower()
nome_inv = nome[::-1]
qnt = nome.count('a')
p = nome.find('a')
u = nome_inv.find('a')
u = len(nome)-u-1
print(f'O seu nome é {nome.capitalize()}\n'
      f'O seu nome invertido é {nome_inv.capitalize()}\n'
      f'A letra A aparece {qnt} vezes\n'
      f'A primeira letra A aparece na posição {p}\n'
      f'A última letra A aparece na posição {u}')
