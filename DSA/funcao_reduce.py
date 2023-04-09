"""REDUCE IRÁ "REDUZIR" UMA LISTA DE ARGUMENTOS (NORMLMENTE NÚMEROS) A UM ELEMENTO
ASSIM COMO O MAP ELE IRÁ EXECUTAR COM UMA FUNÇÃO + LISTA = REDUCE(FUNÇÃO,LISTA).
NOS EXEMPLOS ABAIXO O REDUCE "EXECUTOU" AS FUNÇÕES DEFINIDAS PERCORRENDO TODOS OS ELEMENTOS DA LISTA, ATÉ APRESENTAR
O RESULTADO FINAL"""
from functools import reduce
# numeros = [25, 20, 15, 10, 5]
#
# def subtracao(x, y):
#     return x - y
#
#
# def divisao(x, y):
#     return x / y
#
#
# reducao1 = reduce(subtracao, numeros)
# reducao2 = reduce(divisao, numeros)
# print(f'{reducao1} e {reducao2}')

"""NESSE CASO NÃO DEFINIMOS UMA FUNÇÃO ANTERIOR E USAMOS O LAMBDA PARA EXECUTAR O REDUCE"""
#REDUCE USANDO O LAMBDA
list = [2, 4, 6, 8, 10]
soma = reduce(lambda x, y: x + y, list)
print(soma)

