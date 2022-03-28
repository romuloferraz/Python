times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(times[0:5])
print(times[-4:])
print(sorted(times))
print(sorted(times)[::-1])
print(times.count('Chapecoense'))
#time = 'Chapecoense'
time = input('Digite o nome do time...\n')
print(f"{time} está em {times.index(time) + 1}° lugar")
