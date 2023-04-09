"""a função zip 'concatena' conjunto de valores (listas, tuplas, dicionários), é necessário determinar qual o seu
retorno (list, tuple, dict). Ela somente irá concatenar valores 'encontrados' não concatenando os demais"""

# x = [1, 2, 3]
# y = [4, 5, 6]
# print(list(zip(x, y)))

# Por não ter elementos suficientes o '1' ficou para fora da concanetação
# w = [5, 6]
# z = [9, 0, 1]
# print(list(zip(w, z)))

# USANDO DICIONÁRIOS
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
print(list(zip(dict1, dict2)))  # por não determinar o que era para concatenar o zip unuiu as keys automaticamente
print(list(zip(dict1.values(), dict2.values())))  # ao determinar que somente queria os values, a concatenização foi
# correta
print(list(zip(dict1.items(), dict2.items())))



