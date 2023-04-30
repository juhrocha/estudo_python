import numpy as np
# # Principal objetivo fatiamento das informações
# # matriz = np.array([[1, 2, 3], [4, 5, 6]])
# # print(matriz)
# # matriz1 = np.ones((3, 4))
# # print(matriz1)
# listas = [[1, 2, 3], [4, 3, 2], [0, 2, 4]]
# # Principal objetivo operações matemáticas
# matriz2 = np.matrix(listas)
# print(matriz2)
# print(np.shape(matriz2))
# # Para buscar um valor na matriz por meio de indexação usar [posição da linha, posição da coluna]. Essa indexação
# # tbm tem início na posição 0
# print(matriz2[1, 1])
# print(matriz2[0:2, 1])
# # Alterando um elemento da matriz por meio da indexação
# matriz2[1, 0] = 10
# print((matriz2))
# dtype determina o formato do array qdo chamado dessa forma
matriz3 = np.array([[2, 4, 6, 8], [1, 3, 5, 7]], dtype=float)
print(matriz3)
matriz4 = np.array([[0, 1, 2, 3], [9, 8, 7, 6]])
# dtype trazendo o formato array dessa forma
print(matriz3.dtype, matriz4.dtype)
# verifica o tamanho da matriz
print(matriz3.itemsize, matriz4.itemsize)


