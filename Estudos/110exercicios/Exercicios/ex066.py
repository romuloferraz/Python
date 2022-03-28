num = cont = s = 0
while num != 999:
    num = int(input('Digite um número [999 p/ PARAR]: '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'Você digitou {cont} números e a soma deles é {s}')
