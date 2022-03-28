from random import choice
nome1 = input('Digite o 1° nome:\n')
nome2 = input('Digite o 2° nome:\n')
nome3 = input('Digite o 3° nome:\n')
nome4 = input('Digite o 4° nome:\n')
nomes = (nome1, nome2, nome3, nome4)
print(f'O nome sorteado foi:\n{choice(nomes)}')
