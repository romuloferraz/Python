import random
cont = 0
num1 = random.randint(1, 10)
num2 = int(input('Tente adivinhar o número que estou pensando!\n'))
while num1 != num2:
    if num1 > num2:
        num2 = int(input('Maior... tente outra vez!\n'))
    else:
        num2 = int(input('Menor... tente outra vez!\n'))
    cont += 1
print(f'Acertou! Você precisou de {cont} tentativas!')


