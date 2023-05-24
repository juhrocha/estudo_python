import pandas as pd
dados = pd.read_csv('/home/juliana/Documentos/testecsv.csv')
# Query é o resultado de uma pesquisa, com determinados filtros
df = dados.query('numero2 < 9')
print(df)
# 'isin'verifica se as codições informadas são verdadeiras ou falsas
df = dados['numero1'].isin([0, 1, 2])
print(df)
# Filtra a pesquisa utilizando condições, exemplo: & - ambas condições apresentadas devem ser vdd, | - uma das duas
# condições devem ser vdd, != - resultado diferente das condições descritas, entre outras
df1 = dados.query('UF == "SP" | IDH == "2"')
print(df1)
'''A função groupby no pandas precisa ser acompanhada de algum tipo de agregação, dessa forma será possível compactar 
 os dados. Exemplos de agregação: sum, mean, count, get_group '''
df2 = dados.groupby(['UF', 'Nome']).get_group('DF')
print(df2)
'''Para aplicar mais tipos de agregações devemos utilizar a função agg'''
df3 = dados.groupby('UF').agg({'Idade': 'sum', 'IDH': 'mean'})
print(df3)
