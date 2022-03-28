salario = float(input('Insira seu salário atual: '))
if salario <= 1250:
    salario = salario*1.15
else:
    salario = salario*1.10
print(f'Seu novo salário será = R$ {salario}')
