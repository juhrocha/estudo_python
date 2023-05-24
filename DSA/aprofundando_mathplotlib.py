import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
# Gráfico de linhas
"""O gráfico de linhas deve estar numa dimensão 2D, por isso o uso da biblioteca numpy """
# x = np.array([1, 2, 3, 4, 5, 6, 7])
# y = x*2
# plt.plot(x, y, color='red')
# plt.show()

# Gráfico de colunas
"""plt.legenda insere legendas no gráficos, pois mesmo se definido em label, não aparecerá"""
# x = (20, 10, 5)
# y = (25, 6, 11)
# plt.bar(x, y, label='Barras', color='blue')
# plt.legend()
# plt.show()

# Gráfico de dispersão
"""a personalização por cor tbm pode ser feita por meio de códigos, já tabelados"""
# plt.scatter(x, y, label='Pontos', color='g', marker='*')
# plt.legend()
# plt.show()

# Gráfico de área empilhada
# z = (10, 11, 15)
# plt.stackplot(x, z, y, colors=['red', 'blue', 'black'])
# plt.show()

# Gráfico de pizza
"""é possível utilizar variaveis na construção de gráficos. startangle determina o ângulo de exibição do gráfico e 
explode 'salta uma das fatias da pizza"""
# legendas = ('1', '2', '3')
# plt.pie(x, labels=legendas, startangle=90, explode=(0, 0.1, 0))
# plt.show()

# Gráfico histograma
# idades = [65, 26, 67, 50, 47, 73, 58, 94, 12, 22, 12, 95, 25, 13, 61, 41, 24, 95,
#           17, 66, 60, 73, 26, 54, 16, 76, 83, 12, 15, 35, 54, 11, 61]
# plt.title('Idades de um grupo')
# plt.xlabel('Idade')
# plt.ylabel('Frequência Absoluta')
# plt.hist(idades, 10, rwidth=0.9)
# plt.xlim(min(idades), max(idades))
# plt.show()

# Gráfico 3D
"""Para criação de gráficos 3D é necessário utilizar a biblioteca 'from mpl_toolkits.mplot3d import axes3d'.
 Inicialmente criamos a variavel da figura a ser criada e determinamos sua variação em 3D"""
fig = plt.figure()
# NO subplot determinas as 3 dimenções
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.10)
# wireframe determina que o gráfico não será preenchido, 'tride' é o método de configuração das linhas
ax.plot_wireframe(X, Y, Z, rstride=15, cstride=15)
plt.show()
