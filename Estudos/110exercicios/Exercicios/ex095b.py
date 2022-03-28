time = []
partidas = 0
while True:
    resp =' '
    jogador = {}
    jogador["nome"] = input('Nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador["gols"] = []
    jogador["total"] = 0
    for i in range(0, partidas):
        jogador["gols"].append(int(input(f'Quantos gols {jogador["nome"]} fez na {i+1}ª partida? ')))
        jogador["total"] += jogador["gols"][i]
    time.append(jogador.copy())
    jogador.clear()
    while resp not in 'sSnN':
        resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp in 'nN':
        break
print('-='*30)
print(f'{"cod": >3} {"nome": <16} {"gols ": <16} {"total": <5}')
print('-'*43)
for k, v in enumerate(time):
    print(f'{k: >3}', end=' ')
    for d in v.values():
        print(f'{str(d): <16}', end=' ')
    print()
print('-='*30)
num = int(input('Mostrar dados de qual jogador? [999 p/ sair]\n'))
print(f' -- LEVANTAMENTO DO JOGADOR {time[num]["nome"]} --')
for i, j in enumerate(time[num]["gols"]):
    print(f'    No jogo {i+1} fez {j} gols.')
