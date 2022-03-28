preco = float(input('======== SUPERMERCADO ========\n'
                    'CUSTO TOTAL DAS COMPRAS: R$'))
pgto = int(input('Esolha uma forma de pagamento:\n'
                 '[1] Dinheiro à vista\n'
                 '[2] Cartão à vista\n'
                 '[3] Cartão 2X\n'
                 '[4] Cartão 3X ou mais\n'))
if pgto == 1:
    total = preco*0.9
elif pgto == 2:
    total = preco*0.95
elif pgto == 3:
    total = preco
elif pgto == 4:
    total = preco*1.2
else:
    print('Não existe essa forma de pagamento.')
if 1 <= pgto <= 4:
    print(f'O total a pagar é de {total}')
