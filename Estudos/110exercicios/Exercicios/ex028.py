import random
from random import choice
num2 = int(input('Estou pensando em um número inteiro de 0 a 5, adivinhe qual!\n'))
list = [0,1,2,3,4,5]
num1 = random.choice(list)
if num2 < 0 or num2 > 5:
    print('Eu disse de 0 a 5!')
else:
    if num1 == num2:
        print('Parabéns! Você acertou!')
    else:
        print(f'Errou! Eu pensei no {num1}, não no {num2}!')
