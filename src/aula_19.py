dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
print(dados['nome']) # printa-se um item em especial assim
print(dados['idade'])
dados['genero'] = 'F' # adc items dessa forma
print(dados)
del dados['idade'] # deleta-se um item do dicionário assim
print(dados)

filmes = {'titulo': 'Pulp Fiction', 'ano': 1992, 'diretor': 'Quentin Tarantino'
}
print(filmes.values()) # exibe o conteúdo do dicionário
print(filmes.keys()) # exibe o título do dicionário
print(filmes.items()) # exibe todos itens
for keys, values in filmes.items(): # forma de usar o for para analisar itens individuais do dicionário
    print(f'O {keys} é {values}')

brasil = []
estado1 = {'UF': 'São Paulo', 'sigla': 'SP'}
estado2 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado3 = {'UF': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
# forma de criar um dicionário dentro de uma lista
print(estado1['UF'])
print(estado2['sigla'])
print(estado3)
print(brasil)
print(brasil[0]['UF']) # forma de printar uma item em especial da lista dicionário
print(brasil[2]['sigla'])
print(brasil[1])

estado = {}
brasil = []
for cont in range (0,3):
    estado['UF'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for cont in brasil:
    for key, value in estado.items():
        print(f' O {key} é {value}')
print('FIM')
