def fatorial(n, show=False):
    """
    A funação fatorial() calcula o fatorial de um número n
    :param n: número para se calcular o fatorial.
    :param show: True - mostra os cálculos, False - padrão, não mostra.
    :return: retorna o fatorial de n.
    """
    fat = 1
    print('-'*20)
    for i in range(n, 0, -1):
        fat *= i
        if show == True:
            print(f'{i} ', end='')
            if i > 1:
                print('X ', end='')
            else:
                print('= ', end='')
    return fat

print(fatorial(6, True))
