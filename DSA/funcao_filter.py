"""ASSIM COMO O NOME JÁ DIZ, A FUNÇÃO FILTER IRÁ FILTRAR ELEMENTOS DE UMA LISTA CONTANTO QUE ESTEJAM DE ACORDO COM
AS CONDIÇÕES ESTIPULADAS. EXPRESSA EM FILTER(FUNÇÃO, INTERADOR), ASSIM COMO NO MAP DEVERÁ SER ESTIPULDO
O TIPO A SER RETORNADO (NORMALMENTE LISTA)"""
# def par(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# par_numeros = list(filter(par, numeros))
# print(par_numeros)


#USANDO LAMBDA
par_numeros = list(filter(lambda num: num % 2 == 0, numeros))
print(f'{par_numeros} nova lista')

