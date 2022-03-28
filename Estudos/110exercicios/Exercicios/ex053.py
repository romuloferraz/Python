frase1 = input('Digite uma palavra ou frase para testar:\n')
frase2 = ''.join(frase1.split()).lower()
frase3 = frase2[::-1]
print(frase2)
print(frase3)
if frase2 == frase3:
    print(f'"{frase1}" É um palíndromo')
else:
    print('Não é um palídromo')

