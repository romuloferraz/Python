nome = input('Digite algo:\n')
#print(type(nome))
print(f'O tipo primitivo é {type(nome)}')
print(f'Só tem espaços? {nome.isspace()}')
print(f'É um número {nome.isnumeric()}')
print(f'É alfanumérico? {nome.isalnum()}')
print(f'Está em maiúsculas? {nome.isupper()}')
print(f'Está em minuscúlas? {nome.islower()}')
print(f'Está capitalizada? {nome.istitle()}')

