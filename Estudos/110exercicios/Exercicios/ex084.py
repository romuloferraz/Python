pessoas = []
dados = []
pesos = []
resp = ' '
cont = 0
while True:
    nome = input('Nome: ').strip().capitalize()
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    pesos.append(peso)
    dados.clear()
    cont += 1
    while resp not in 'nNsS':
        resp = input('Deseja continuar? [S/N] ').strip().upper()
    if resp in 'nN':
        break
    resp = ' '
print(f'Foram cadastradas {cont} pessoas')
print(pessoas)
max = max(pesos)
max_index = pesos.index(max)
min = min(pesos)
min_index = pesos.index(min)
print(f'O mais pesado é {pessoas[max_index][0]} com {max} Kg')
print(f'O mais leve é {pessoas[min_index][0]} com {min} Kg')
