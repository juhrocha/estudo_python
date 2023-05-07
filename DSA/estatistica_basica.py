import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6])
print(array1.mean())  # média artmética
print(array1.max())
print(array1.std())  # desvio padrão
print(array1.min())
print(array1.var())  # variância
print(array1.sum())  # soma
print(array1.prod())  # multiplicação
print(array1.cumsum())  #soma acumulada
array2 = np.array([10, 9, 8, 7, 6, 5])
print(np.add(array1, array2))  # soma de duas arrays
print(np.dot(array1, array2))  # multiplica duas arrays
print(array1 @ array2)  # tbm multiplica duas arrays

