medida = float(input('Uma distância em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print(f'A medida de {medida}m corresponde a...\n'
      f'{km}km\n'
      f'{hm}hm\n'
      f'{dam}dam\n'
      f'{dm}dm\n'
      f'{cm}cm\n'
      f'{mm}mm\n')
