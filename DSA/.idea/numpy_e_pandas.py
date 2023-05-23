import pandas as pd
dicionario = {'Estados': ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Sergipe'], 'Ano': [2000, 2006, 1992, 1980],
              'Taxa de desemprego': [1.89, 2, 0.47, 1.5]}
df = pd.DataFrame(dicionario)
# Resumo estatístico de colunas númericas
# print(df.describe())
df2 = pd.DataFrame(dicionario, columns=['Estados', 'Ano', 'Cidade', 'Taxa de desemprego'])
# Verifica se há valores ausentes
# print(df2.isna())
import numpy as np
df2['Cidade'] = np.arange(0.5)
print(df2)