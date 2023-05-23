# TODO: CÓDIGO
import pandas as pd
dados = pd.read_csv('/home/juliana/Documentos/testecsv.csv')
# # Query é o resultado de uma pesquisa, com determinados filtros
# # df = dados.query('numero2 < 9')
# # print(df)
# # 'isin'verifica se as codições informadas são verdadeiras ou falsas
# df = dados['numero1'].isin([0, 1, 2])
# print(df)
df1 = [(dados.UF == 'SP') | (dados.IDH == 2)]
print(df1)






