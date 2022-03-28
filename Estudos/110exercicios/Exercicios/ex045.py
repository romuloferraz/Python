import random
from time import sleep
jogada = int(input('Esolha uma opção:\n'
                   '[1] PEDRA\n'
                   '[2] PAPEL\n'
                   '[3] TESOURA\n'))
pc = random.randint(1, 3)
jogo = (jogada, pc)
vitoria = ((1, 3), (2, 1), (3, 2))
derrota = ((3, 1), (1, 2), (2, 3))
empate = ((1, 1), (2, 2), (3, 3))
sleep(0.5)
print('JO...')
sleep(1)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
if jogo in vitoria:
    print('VOCÊ VENCEU')
elif jogo in derrota:
    print('DERROTA! PC GANHOU!')
elif jogo in empate:
    print('EMPATE!')
