casa = float(input('Qual o valor da casa?\n'))
salario = float(input('Qual o seu salário?\n'))
anos = int(input('Em quantos anos pretende quitar a casa?\n'))
parcela = casa/(anos*4)
if (parcela>0.3*salario):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('Empréstimo concedido!')
