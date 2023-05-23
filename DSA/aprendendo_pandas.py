import pandas as pd
dicionario = {'Estados': ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Sergipe'], 'Ano': [2000, 2006, 1992, 1980],
              'Taxa de desemprego': [1.89, 2, 0.47, 1.5]}

# df = pd.DataFrame(dicionario)
# print(df)
## Reorganizando a ordem das colunas
# df = pd.DataFrame(dicionario, columns=['Ano', 'Estados', 'Taxa de desemprego'])
# print(df)
## Acrescentando colunas e renoneando indexador
df2 = pd.DataFrame(dicionario, columns=['Estados', 'Ano', 'Cidade', 'Taxa de desemprego'], index=['estado1', 'estado2',
                                                                                                  'estado3', 'estado4'])
# print(df2)
## Filtrando informações pelo indexador (renomeado anteriormente)
print(df2.filter(items=['estado1'], axis=0))





