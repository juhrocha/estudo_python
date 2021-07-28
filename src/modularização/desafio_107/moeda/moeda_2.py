def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
    # substitui . por ,


def aumentar(valor, taxa, formatado=False):
    aumento = valor+(valor*taxa/100)
    return aumento if formatado is False else moeda(aumento)


def diminuir(valor, taxa, formatado=False):
    reducao = valor - (valor*taxa/100)
    return reducao if formatado is False else moeda(reducao)


def dobro(valor, formatado=False):
    double = valor*2
    return double if formatado is False else moeda(double)


def metade(valor, formatado=False):
    half = valor/2
    return half if formatado is False else moeda(half)


def titulo(txt):
    print('*'*30)
    print(txt.center(30))
    print('*' * 30)


def resumo(valor, aumento=0, diminuicao=0):
    titulo(f'RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{diminuicao}% de redução: \t{diminuir(valor, diminuicao, True)}')
    print('*'*30)

