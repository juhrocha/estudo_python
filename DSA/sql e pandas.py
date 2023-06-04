import sqlite3
import pandas as pd
con = sqlite3.connect('/home/juliana/Documentos/cap12_dsa.db')
cursor = con.cursor()
# query = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
#          FROM tb_vendas_dsa
#          WHERE Valor_Unitario > 199
#          GROUP BY Nome_Produto'''
# dados = cursor.execute(query)
# df = pd.DataFrame(dados, columns=['Nome_produto',
#                                   'Unidades_vendidas'])
query1 = 'SELECT * FROM tb_vendas_dsa'
dados1 = cursor.execute(query1)
df1 = pd.DataFrame(dados1)
print(df1.head())
