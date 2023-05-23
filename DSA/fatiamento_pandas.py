import pandas as pd
dicionario = {'Estados': ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Sergipe'], 'Ano': [2000, 2006, 1992, 1980],
              'Taxa de desemprego': [1.89, 2, 0.47, 1.5]}
df = pd.DataFrame(dicionario)
## Fatiamento convencional
# print(df[1:3])
df2 = pd.DataFrame(dicionario, index=['estado1', 'estado2', 'estado3', 'estado4'])
## Fatiamento com indexador nomeado
# print(df2['estado1':'estado3'])
## Fatiamento condicional
"""Ao fazer esse tipo de fatiamento é necessário definir com dois colchetes"""
# print(df2[df2['Ano'] > 2000])
print(df2[['Ano', 'Taxa de desemprego']])


