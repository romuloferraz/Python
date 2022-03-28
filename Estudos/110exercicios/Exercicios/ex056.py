S_idade = 0
maiorM = 0
cont_F = 0
for i in range(0, 4):
    print(f'------ {i+1}ª PESSOA ------')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ')
    S_idade += idade
    if sexo.capitalize() == 'M':
        if idade > maiorM:
            maiorM = idade
            nomeM = nome
    if sexo.capitalize() == 'F':
        if idade < 20:
            cont_F += 1
media = S_idade/4
print(f'A média de idade do grupo é {media}\n'
      f'O homem mais velho tem {maiorM} anos e se chama {nomeM}\n'
      f'Ao todo são {cont_F} mulheres com menos de 20 anos')


