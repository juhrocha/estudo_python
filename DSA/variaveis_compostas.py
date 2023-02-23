#LISTA
frutas = ['maça', 'banana', 'kiwi', 'pera']
print(frutas)
print(len(frutas))
print(frutas[:2])
print(frutas[-1])
frutas.append('goiaba')
frutas[1] = 'figo'
print(frutas)
print(len(frutas))
print(sorted(frutas))

#DICIONÁRIO
dados = {'Juliana': 29,
         'Reinaldo': 30,
         'Maria': 65}

print(dados['Juliana'])
print(dados['Maria'])

dados['João'] = 90
print(dados)
print(dados.keys())
print(dados.values())
for keys, values in dados.items():
    print(f'{keys} tem {values} anos')
print('FIM')

#TUPLA
numeros = (1, 2, 3, 4)
print(len(numeros))
print(max(numeros))
print(min(numeros))
print(numeros[:2])
print(numeros[-1])
print(numeros)
for valor in numeros:
    print(f' O número {valor} multiplicado por 2 é igual a {valor * 2}')


# LISTA + DICIONÁRIO
chaves = {'c1': [1, 2, 3], 'c2': [4, 5, 6], 'c3': [7, 8, 9]}
print(chaves['c1'])
print(chaves['c2'])
print(chaves['c3'][1])
