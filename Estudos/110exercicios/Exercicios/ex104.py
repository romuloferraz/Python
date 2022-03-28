def leiaInt(msg):
    num = input(msg)
    while num.isnumeric() == False:
        print("\033[1;31mERRO! Digite um número válido.\033[m")
        num = input(msg)
    return num




#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
