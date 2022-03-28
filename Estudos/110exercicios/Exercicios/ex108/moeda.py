def aumentar(n, a):
    res = n + a
    return res
def diminuir(n, a):
    res = n - a
    return res
def dobro(n):
    res = 2 * n
    return res
def metade(n):
    res = n / 2
    return res
def moeda(num):
    num = f'R${num: .2f}'
    return num.strip().replace('.', ',')
