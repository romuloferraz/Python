from random import sample
def embaralha(nome):
    a = sample(nome, len(nome))
    d = ''.join(a)
    print(a)
    print(d.lower())


nome = input('Digite algo: ')
embaralha(nome)
