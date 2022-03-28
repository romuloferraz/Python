time = []
cod = 0
while True:
    resp =' '
    jogador = {}
    jogador["cod"] = cod
    cod += 1
    jogador["nome"] = input('Nome do jogador: ').strip().capitalize()
    jogador["partidas"] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador["gols"] = []
    for i in range(0, jogador["partidas"]):
        jogador["gols"].append(int(input(f'Quantos gols {jogador["nome"]} fez na {i+1}ª partida? ')))
    time.append(jogador.copy())
    jogador.clear()
    while resp not in 'sSnN':
        resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp in 'nN':
        break
print('-='*30)
print(f'{"cod ": >3}{"nome": <16}{"gols ": <16}{"total": <5}')
print('-'*43)
for i in time:
    print(f'{i["cod"]: >3}', end='')
    print(f' {i["nome"]: <16}', end='')
    print(f'{str(i["gols"]): <16}', end='')
    s = 0
    for j in i["gols"]:
        s += j
    print(f'{s: <5}')
print('-='*30)
num = int(input('Mostrar dados de qual jogador? [999 p/ sair]\n'))
print(f' -- LEVANTAMENTO DO JOGADOR {time[num]["nome"]}')
for i, j in enumerate(time[num]["gols"]):
    print(f'    No jogo {i+1} fez {j} gols.')
