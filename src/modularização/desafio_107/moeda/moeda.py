def aumentar(numero, taxa):
    aumento = numero+(numero*taxa/100)
    return aumento


def diminuir(numero, taxa):
    reducao = numero-(numero*taxa/100)
    return reducao


def dobro(numero):
    return numero*2


def metade(numero):
    return numero/2


def moeda(numero):
    return f'R$ {numero:.2f}'.replace('.', ',')
    # substitui . por ,

