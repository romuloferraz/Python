def area(x, y):
    print(f'A área de um terreno {x} X {y} é {x*y}m².')
def interface(msg):
    print('-'*30)
    print(f'{str(msg).strip().upper(): ^30}')
    print('-'*30)
interface('controle de terreno')
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
area(largura, comprimento)
