import math
alfa = float(input('Digite o ângulo procurado, em graus: '))
sinalfa = math.sin(math.radians(alfa))
cosalfa = math.cos(math.radians(alfa))
tanalfa = math.tan(math.radians(alfa))
print(f'O seno de {alfa}° é.....{sinalfa:.3f}\n'
      f'O coseno de {alfa}° é...{cosalfa:.3f}\n'
      f'A tangente de {alfa}° é {tanalfa:.3f}')

