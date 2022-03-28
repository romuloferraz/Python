expressao = input('Digite uma expressão para ser analisada:\n')
cont1 = expressao.count('(')
cont2 = expressao.count(')')
print(cont1, cont2)
if cont1 != cont2:
    print('Expressão ERRADA!')
