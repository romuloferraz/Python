list = []
for i in range(1, 6):
    peso = float(input(f'Qual o {i}° peso? '))
    list.append(peso)
maior = max(list)
menor = min(list)
print(f'O menor peso é {menor} Kg\n'
      f'O maior peso é {maior} Kg')
