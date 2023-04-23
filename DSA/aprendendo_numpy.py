import numpy as np
# MANIPULAÇÃO DE INDEXAÇÃO
# lista = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(lista)
# print(lista.shape)
# print(lista[2])
# indices = [1, 5, 8]
# print(lista[indices])
# par = (lista % 2 == 0)
# print(lista[par])
# lista[0] = 10
# print(lista)

# USANDO FUNÇÕES BUILT IN DO NUMPY
# lista1 = np.array([1, 2, 3, 4, 5, 6])
# print(lista1)
# print(lista1.cumsum())
# print(lista1.cumprod())
# print(lista1.max())
# print(lista1.mean())
# lista2 = np.arange(0, 50, 5)
# print(lista2)
# print(lista2.size)
# print(lista2.nonzero())
# print(lista2)
lista3 = np.eye(3)
print(lista3)
lista4 = np.diag(np.array([1, 2, 3, 4, 5, 6]))
print(lista4)
