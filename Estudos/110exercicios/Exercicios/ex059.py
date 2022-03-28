import os
import time

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('[1] Somar\n'
                  '[2] Subtrair\n'
                  '[3] Multiplicar\n'
                  '[4] Dividir\n'
                  '[5] Sair do programa\n'
                  'Qual é a sua opção?\n'))
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif opcao == 3:
        print(f'{num1} x {num2} = {num1*num2}')
    elif opcao == 4:
        print(f'{num1} / {num2} = {(num1/num2):.2f}')
    print('='*60)
    time.sleep(1)
    os.system('cls')
    #time.sleep(1)
print('FIM')
