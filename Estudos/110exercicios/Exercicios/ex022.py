nome = input('Digite o seu nome completo: ').strip()
len_nome = len(nome.split())
print(f'O seu nome próprio possui {len_nome} palavras')
qt_letras = 0
for c in range(0,len_nome):
    print(f'Nome {c+1}: {nome.split()[c]}')
    qt_letras = qt_letras + len(nome.split()[c])
print(f'Seu nome em maiúsculas é {nome.upper()}\n'
      f'Seu nome em minúsculas é {nome.lower()}\n'
      f'Seu nome tem ao todo {qt_letras} letras\n'
      f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras\n')
