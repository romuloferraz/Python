import random

venceu = True
print('Vamos jogar um jogo? Par ou Ímpar!')
while venceu == True:
    num1 = int(input('Escolha um número de 1 a  10: '))
    opcao1 = input('Par ou Ímpar? [P/I]').strip().upper()
    num2 = random.randint(1, 10)
    if opcao1 == 'P':
        if (num1 + num2) % 2 == 0:
            venceu = True
            print('Parabéns vc venceu')
        else:
            venceu = False
            print('Você perdeu!\n')
            break
    else:
        if (num1 + num2) % 2 != 0:
            venceu = True
            print('Parabéns vc venceu')
        else:
            venceu = False
            print('Você perdeu!\n')
            break
print(f'Você: {num1} e {opcao1}// PC: {num2}')
print('FIM DE JOGO!')





