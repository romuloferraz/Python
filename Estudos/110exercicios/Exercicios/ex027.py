nome = input('Digite aqui seu nome: ').strip()
list = nome.split()
u = len(list)-1
print(f'Seu primeiro nome é: {list[0]}\n'
      f'Seu último nome é: {list[u]}')

