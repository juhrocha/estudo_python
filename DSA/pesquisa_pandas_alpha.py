import pandas as pd
dados = pd.read_csv('/home/juliana/Documentos/testecsv.csv')
'''Basicamente, usaremos a seguinte construção para aplicar os métodos de strings: dados[‘Coluna’].str.metodo()

a) dados[‘Coluna’]: selecionar a coluna de interesse

b) .str: adicionar o str accessor

c) .metodo(): aplicar o método'''

df = dados['Cidade'].str.startswith('S')
print(df)
df1 = dados['Cidade'].str.lower()
print(df1)
df2 = dados['Gênero'].str.endswith('c')
print(df2)
df3 = dados['Nome'].str.split('a').str[1:]
print(df3)
df4 = dados['UF'].str.split('A')
print(df4)
df5 = dados['Nome'].str.strip('J')
print(df5)
df6 = dados['Nome'].str.replace('J', 'j')
print(df6)
df7 = dados['Cidade'] = dados['Cidade'].str.cat(dados['UF'], sep=', ')
print(df7)
