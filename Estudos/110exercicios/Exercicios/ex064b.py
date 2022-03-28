num = cont = 0
s = 0
num = int(input('Digite um número [999 para PARAR]: '))
while num != 999:
    s = s + num
    cont += 1
    num = int(input('Digite um número [999 para PARAR]: '))
print(f'Você digitou {cont} números e a soma deles é {s}')
