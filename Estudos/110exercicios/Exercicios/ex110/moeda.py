def aumentar(n, t, f=False):
    res = n + (n * t)/100
    if f == True:
        return moeda(res)
    else:
        return res


def diminuir(n, t, f=False):
    res = n - (n * t)/100
    if f == True:
        return moeda(res)
    else:
        return res


def dobro(n, f=False):
    res = 2 * n
    if f == True:
        return moeda(res)
    else:
        return res


def metade(n, f=False):
    res = n / 2
    if f == True:
        return moeda(res)
    else:
        return res


def moeda(num):
    num = f'R${num: .2f}'
    return num.strip().replace('.', ',')

def resumo(num):
    print('-'*30)
    print(f'{"RESUMO DO VALOR": ^30}')
    print('-'*30)
    print(f"{'Preço analisado: ': <20}{moeda(num): <10}")
    print(f"{'Dobro do preço: ': <20}{dobro(num, True): <10}")
    print(f"{'Metade do preço: ': <20}{metade(num, True): <10}")
    print(f"{'80% de aumento: ': <20}{aumentar(num, 80, True): <10}")
    print(f"{'35% de redução: ': <20}{diminuir(num, 80, True): <10}")
