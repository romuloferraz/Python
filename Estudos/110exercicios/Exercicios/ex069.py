print('='*40)
print('CADASTRO DE PESSOAS')
print('='*40)
mais_18 = 0
hom = 0
mul_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        hom += 1
    elif sexo == 'F':
        if idade < 20:
            mul_20 += 1
    resp = input('Quer continuar cadastrando? [S/N]').upper().strip()[0]
    if resp == 'N':
        break
    print('*'*40)
print('FIM DO CADASTRO!')
print(f'Total de pessoas com mais de 18 anos: {mais_18}\n'
      f'Homens cadastrados: {hom}\n'
      f'Mulheres com menos de 20 anos: {mul_20}\n')


