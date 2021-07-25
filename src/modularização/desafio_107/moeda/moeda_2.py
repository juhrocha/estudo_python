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

