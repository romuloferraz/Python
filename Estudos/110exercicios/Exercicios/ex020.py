import random
n1 = str(input('Digite o 1° nome: '))
n2 = str(input('Digite o 2° nome: '))
n3 = str(input('Digite o 3° nome: '))
n4 = str(input('Digite o 4° nome: '))
nomes = [n1, n2, n3, n4]
random.shuffle(nomes)
print('A ordem de apresentação será:\n')
print(nomes)
