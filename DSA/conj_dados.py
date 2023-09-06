import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Abrindo um arquivo csv
arquivo = pd.read_csv('/home/juliana/Área de Trabalho/dataset.csv')
#
# # Utilizando algumas funções do pandas
# print(arquivo.describe)
# print(arquivo.corr())
# print(arquivo.columns)
#
# # Aplicando uma função em uma coluna específica
# print(arquivo['valor_aluguel'].describe)

# # Criando histograma com os dados
# sns.histplot(data=arquivo, x=arquivo['valor_aluguel'], kde=True)
# plt.show()

X = np.array(arquivo['area_m2'])
X = X.reshape(-1, 1)
y = arquivo['valor_aluguel']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state= 42)
# print(X_treino.shape)
# print(X_teste.shape)

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
# Gráfico
# plt.scatter(X, y)
# Utilizar o plot permite que a linha seja inserida no gráfico scatter
# plt.plot(X, modelo.predict(X), color= 'red')
# plt.show()

# Cálculo de coeficiente de relação
score = modelo.score(X_teste, y_teste)
print(f'Coeficiente R^2: {score:.2f}')


