sexo = input('Digite o sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Opção inválida! digite o sexo [M/F]').upper().strip()
print(f'Sexo {sexo} registrado com sucesso')
