cadastro = []
pessoa = {}
s = 0
mulheres = []
acima_media = []
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').upper().strip()
    while pessoa['sexo'] not in 'mMfF':
        pessoa['sexo'] = input('ERRO! Por favor, responda apenas M ou F: ').upper().strip()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    cadastro.append(pessoa.copy())
    pessoa.clear()
    resp = input('Quer continuar? [S/N] ').upper().strip()
    while resp not in 'nNsS':
        resp = input('ERRO! Por favor, responda apenas S ou N: ')
    if resp in 'nN':
        break
print('-='*30)
print(f'Ao todo temos {len(cadastro)} pessoas cadastradas.\n'
      f'A média de idade é de {s/len(cadastro)} anos.\n'
      f'As mulheres cadastradas foram: {mulheres} \n'
      f'\nLista de pessoas que estão acima da média:')
for p in cadastro:
    if p['idade'] > s/len(cadastro):
        for k, v in p.items():
            print('    ', end='')
            print(f'{k} = {v}; ', end='')
        print()
print('\n<< ENCERRADO >>')
