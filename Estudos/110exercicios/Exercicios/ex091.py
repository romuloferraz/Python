import random

total_jogadas = []
jogada = {}
total_ordenado = []
for i in range(1, 5):
    jogada['nome'] = f'Jogador{i}'
    jogada['dado'] = random.randint(1, 6)
    total_jogadas.append(jogada.copy())
    jogada.clear()
for i in range(0, 4):
    print(f'{total_jogadas[i]["nome"]} tirou {total_jogadas[i]["dado"]} no dado.')
print('-='*20)
print('== RANKING DOS JOGADORES ==')
total_ordenado = sorted(total_jogadas, key=lambda k: k['dado'], reverse=True)
for i in range(0, 4):
    print(f'{i+1}° lugar: {total_ordenado[i]["nome"]} com {total_ordenado[i]["dado"]}.')



