num = cont = 0
s = 0
while num != 999:
    num = int(input('Digite um número [999 para PARAR]: '))
    if num == 999:
        break
    s = s + num
    cont += 1
print(f'Você digitou {cont} números e a soma deles é {s}')
