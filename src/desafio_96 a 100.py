# Exercício 96 - Curso em vídeo - 1ª tentativa
# def area_terreno():
#     print('Controle de Terreros')
#     print('*'*30)
#     largura = float(input('LARGURA (m): '))
#     comprimento = float(input('COMPRIMENTO (m): '))
#     area = largura * comprimento
#     print(f'A área desse terreno é {area:.2f}m²')
#
#
# area_terreno()
# print('FIM')

# Exercício 96 - Curso em vídeo - 2ª tentativa
# def area(largura, comprimento):
#     area_terreno = largura*comprimento
#     print(f'A área desse terro é igual a {area_terreno:.2f}m²')
#
#
# print('Controle de Terreros')
# print('*'*30)
# largura_terreno = float(input('LARGURA (m): '))
# comprimento_terreno = float(input('COMPRIMENTO (m): '))
# area(largura_terreno, comprimento_terreno)

# Exercício 97 - Curso em vídeo
# def escreva(txt):
#     tamanho = len(txt)
#     print('-'*len(txt))
#     print(txt)
#     print('-'*len(txt))
#
#
# escreva('Juliana')
# escreva('Olá Mundo')
# escreva('Oi')

# Exercício 98 - Curso em vídeo - 1ª tentativa
# from time import sleep
# def contador():
#     print('-'*20)
#     print('Contagem de 1 a 10 de 1 em 1:')
#     for cont in range(0, 10):
#         print(f'{cont+1}', end=' ')
#         sleep(0.25)
#     print('Fim!')
#     print('-' * 20)
#     print('Contagem de 10 a 0 de 2 em 2:')
#     for cont in range(10, -2, -2):
#         print(f'{cont}', end=' ')
#         sleep(0.25)
#     print('Fim!')
#     print('-' * 20)
#     print('Agora é sua vez de personalizar a contagem!')
#     inicio = int(input('Início: '))
#     fim = int(input('Fim: '))
#     passo = int(input('Passo: '))
#     print('-' * 20)
#     print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
#     for cont in range(inicio, fim, passo):
#         print(f'{cont}', end=' ')
#         sleep(0.25)
#     print('Fim!')
#     print('-' * 20)
#
#
# contador()

# Exercício 98 - Curso em vídeo - 2ª tentativa
# from time import sleep
# def contador(inicio, fim, passo):
#     print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
#     for count in range(inicio, fim, passo):
#         print(f'{count}', end=' ', flush=True)
#         sleep(0.75)
#     print('Fim!')
#     print('*' * 30)
#
#
# contador(1, 10, 1)
# contador(10, 0, -1)
# print('Agora é sua vez de personalizar a contagem!')
# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))
# contador(inicio, fim, passo)

# Exercício 99 - Curso em vídeo
# from time import sleep
# def mostraLinha():
#     print('*'*20)
#
#
# def maior(*num):
#     print('Analisando os valores informados...')
#     print(f'Foram informados {num} um total de {len(num)} números.')
#     print(f'O maior número informado foi {max(num)}')
#
#
# mostraLinha()
# sleep(1)
# maior(1, 2, 3, 4, 5, 6)
# mostraLinha()
# sleep(1)
# maior(3, 6, 9, 8, 7, 10)
# mostraLinha()
# sleep(1)
# maior(11, 22, 33, 55, 100)

# Exercício 100 - Curso em vídeo
from random import randint
def sorteia(list):
    for count in range(0, 5):
        list.append(randint(0, 10))
    print(f'Os valores sorteador foram: {list}')


def somaPar(list):
    soma = 0
    for valor in list:
        if valor % 2 == 0:
           soma += valor
    print(f'Somando os valores pares de {list}, temos {soma}')


valores = []
sorteia(valores)
somaPar(valores)
# Nesse exercício para a função trabalhar melhor, o print deve ficar em def