listagem = (('Lápis', 1.75),
            ('Borracha', 2.00),
            ('Caderno', 15.90),
            ('Estojo', 25.00),
            ('Transferidor', 4.20),
            ('Compasso', 9.99),
            ('Mochila', 120.32),
            ('Canetas', 22.30),
            ('Livro', 34.90))
print('+'*40)
print(f"{'LISTAGEM DE PREÇOS' : ^40}")
print('+'*40)
for c in listagem:
    print(f'{c[0] :.<30}', end='' 'R$')
    print(f'{c[1] : 8.2f}')
