def aumentar(n, a, f=False):
    res = n + a
    if f == True:
        return moeda(res)
    else:
        return res


def diminuir(n, a, f=False):
    res = n - a
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
