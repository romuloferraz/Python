print('='*30)
print(f"{'LOJA SUPER BARATÃO' : ^30}")
print('='*30)
s = m_mil = cont = 0
while True:
    prod = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    s += preco
    if preco > 1000:
        m_mil += 1
    if cont == 0:
        menor = preco
        barato = prod
    cont += 1
    if preco < menor:
        barato = prod
        menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
print(f'Total da compra: R$ {s}\n'
      f'Temos {m_mil} produto(s) custando mais de R$ 1000\n'
      f'O produto mais barato foi {barato} que custa R${menor}\n')
