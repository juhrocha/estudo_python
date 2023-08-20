import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
# a importação do statsmodel dele ser realizada com .api
import seaborn as sns

# # Subindo o arquivo
df_dsa = pd.read_csv('/home/juliana/Área de Trabalho/dataset.csv')
# # Descrevendo uma coluna
# print(df_dsa['valor_aluguel'].describe())

# # Histograma com Seaborn
# grafico = sns.histplot(data=df_dsa, x='valor_aluguel', kde=True)
# # Para exibir o gráfico é necessário utilizar o plt.show da matplhotlib.pyplot
# plt.show()

# Gráfico de dispersão com Seaborn
# sns.scatterplot(data=df_dsa, x='area_m2', y='valor_aluguel')
# plt.show()

# Regressão linear simples
y = df_dsa['valor_aluguel']
x = df_dsa['area_m2']
X = sm.add_constant(x)
modelo = sm.OLS(y, X).fit()
# # fit e summary são necessários para a exibição do modelo de regressão no statsmodels
# print(modelo.summary())

# Gráfico para regressão acima
plt.scatter(x, y)
plt.plot(x, modelo.fittedvalues, color='r', label='Linha de progressão')
# fittedvalues permite a extração dos valores do modelo de regressão criado
plt.xlabel('Área m2')
plt.ylabel('Valor do aluguel')
plt.legend()
plt.show()




















