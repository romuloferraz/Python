def voto(nasc):
    from datetime import date
    today = date.today().year
    idade = today - nasc
    if idade < 16:
        return f'Com {idade} anos você não pode votar.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos você pode votar, mas não é obrigatório.'
    else:
        return f'Com {idade} anos você é obrigado a votar.'
ano = int(input('Qual o seu ano de nascimento? '))
print(voto(ano))
