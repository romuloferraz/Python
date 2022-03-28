import random

print('='*40)
print(f"{'MEGA SENA DA VIRADA' : ^40}")
print('='*40)
jogo = []
quant = int(input('Quantas surpresinhas gostaria de comprar? '))
for i in range(0, quant):
    for j in range(0, 6):
        num = random.randint(1, 60)
        while num in jogo:
            num =random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f"Jogo {i+1} >> {sorted(jogo)}")
    jogo.clear()

