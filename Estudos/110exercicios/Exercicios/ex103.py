def jogador(_nome='<desconhecido>', _gols=0 ):
    print(f'O jogador {_nome} fez {_gols} gols no camponato.')

nome = input('Nome do jogador: ')
gols = input('Número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if not nome and gols:
    jogador(_gols=gols)
elif nome and not gols:
    jogador(nome)
else:
    jogador(nome, gols)

