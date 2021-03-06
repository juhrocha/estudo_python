# # Exercício 78 - Curso em Vídeo
# numero=list()
# maior = 0
# menor = 0
# for valor in range (0,5):
#     numero.append(int(input('Digite um número: ')))
#     if valor == 0:
#         maior = menor = numero[valor]
#     else:
#         if numero[valor] > maior:
#             maior = numero[valor]
#         elif numero[valor] < menor:
#             menor = numero[valor]
# print(f'Os números digitados foram: {numero}')
# print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')
# for indice, posicao in enumerate(numero):
#     if posicao == maior:
#         print(f'O maior valor está na posição {indice}')
# for indice, posicao in enumerate(numero):
#     if posicao == menor:
#         print(f'O menor valor está na posição {indice}')