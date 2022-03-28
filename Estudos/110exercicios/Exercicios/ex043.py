peso = float(input('Digite o seu peso(Kg): '))
h = float(input('Digite sua altura(m): '))
imc = peso/(h**2)
if imc < 18.5:
    clf = 'abaixo do peso ideal!'
elif imc <25:
    clf = 'no peso ideal!'
elif imc < 30:
    clf = 'sobrepeso!'
elif imc < 40:
    clf = 'obeso!'
else:
    clf = 'obeso mórbido!'
print(f'Seu IMC é {imc:.1f}\n'
      f'e vc está {clf}')
