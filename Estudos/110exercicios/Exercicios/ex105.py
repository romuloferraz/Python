def boletim(* notas, sit=False):
    """
    -> A função realiza análise das notas
    :param notas: recebe quantas notas forem necessárias
    :param sit: booleana para mostrar ou não a situação (padrão = False)
    :return: retorna um dicionário com as notas e situação(opcional)
    """
    dict_notas = {}
    dict_notas["total"] = len(notas)
    dict_notas["maior"] = max(notas)
    dict_notas["menor"] = min(notas)
    dict_notas["média"] = sum(notas)/len(notas)
    if sit == True:
        if dict_notas["média"] < 5:
            dict_notas["situação"] = 'Reprovável'
        elif dict_notas["média"] < 7:
            dict_notas["situação"] = 'Razoável'
        elif dict_notas["média"] < 9:
            dict_notas["situação"] = 'Boa'
        else:
            dict_notas["situação"] = 'Excelente'

    return dict_notas


print(boletim(10, 5, 10, 10, 10, 10, 10, 10, sit=True))
help(boletim)
