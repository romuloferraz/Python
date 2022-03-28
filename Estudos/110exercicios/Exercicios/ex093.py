jogador = {}
jogador['nome'] = input('Nome do jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
jogador['total'] = 0
for i in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['total'] += jogador['gols'][i]
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i in range(0, jogador['partidas']):
    print(f'=> Na partida {i}, fez {jogador["gols"][i]}.')
print(f'Foi um total de {jogador["total"]} gols.')
