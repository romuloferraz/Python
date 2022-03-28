maior = 0
menor = 100000
for i in range(1, 6):
    peso = float(input(f'Qual o {i}° peso? '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O menor peso é {menor} Kg\n'
      f'O maior peso é {maior} Kg')
