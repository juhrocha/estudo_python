import pandas as pd
dados = pd.read_csv('/home/juliana/Documentos/testecsv.csv')
# print(dados.head())
# print(dados.isna())
## O método fillna do pandas preenche valores ausentes, em 'value' determinar o valor a ser preenchido e 'inplace'
## confirmar com True, pois assim ele será salvo no arquivo, sem o True o pandas cria uma cópia do arquivo
# dados['numero3'].fillna(value=6, inplace=True)
# print(dados)

