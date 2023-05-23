import pandas as pd
import numpy as np
dicionario = {'Estados': ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Sergipe'], 'Ano': [2000, 2006, 1992, 1980],
              'Taxa de desemprego': [1.89, 2, 0.47, 1.5]}
df = pd.DataFrame(dicionario)
## Resumo estatístico de colunas númericas
# print(df.describe())
df2 = pd.DataFrame(dicionario, columns=['Estados', 'Ano', 'Taxa de IDH', 'Taxa de desemprego'], index=['estado1', 'estado2',
                                                                                                'estado3', 'estado4'])
## Verifica se há valores ausentes
# print(df2.isna())
## Inclui valores via numpy
df2['Taxa de IDH'] = np.arange(4.)
print(df2)
