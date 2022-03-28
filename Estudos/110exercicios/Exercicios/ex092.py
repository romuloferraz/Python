cadastro = {}
cadastro['nome'] = input('Nome: ')
cadastro['ano'] = int(input('Ano de nascimento: '))
cadastro['carteira'] = int(input('Carteira de Trabalho: '))
cadastro['ano2'] = int(input('Ano de contratação: '))
cadastro['salario'] = input('Salário: R$')
print('-='*30)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')
