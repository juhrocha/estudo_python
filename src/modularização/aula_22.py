# def fatorial(numero):
#     f_inicial = 1
#     for count in range(1, numero+1):
#         f_inicial *= count
#     return f_inicial
#
#
# def dobro(numero):
#     return numero*2
#
#
# def triplo(numero):
#     return numero*3

import funcoes_aula22
numero = int(input('Digite um valor: '))
factorial = funcoes_aula22.fatorial(numero)
double = funcoes_aula22.dobro(numero)
triple = funcoes_aula22.triplo(numero)
print(f'O fatorial de {numero} é {factorial}.\n'
      f'Já o dobro é {double} e o tiplo {triple}')


