"""Para criar gŕaficos na IDE é necessário o pacote matplotlib, já no pacote sklearn buscamos os dados utilizados no
gráfico"""
import sklearn
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
data = load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['species'] = data['target']
# print(df.head())
"""Por ambos métodos do matplotlib é possível um gŕafico e com o plot determinar o tipo de gráfico. Utilizando as 
funções do pandas conseguimos agrupar, por exemplo os dados do gráfico"""
plt.plot(df)
plt.show()

df.groupby('species').mean().plot.bar()
plt.show()

df.groupby('species').mean().plot.line()
plt.show()
