import sqlite3
'''Primeiro é necessário importar a biblioteca sqlite e após é necessário criar a conexão com o arquivo; normalmente
a conexão tem a atribuição "con". Em seguida criamos o cursor, o "local" em que o arquivo será "lido"'''
conexao = sqlite3.connect('/home/juliana/Documentos/cap12_dsa.db')
cursor = conexao.cursor()
'''Com o ambiente criado, podemos fazer querys e executa-las'''
# sql_query = """SELECT * FROM sqlite_master"""
# cursor.execute(sql_query)  # se faz necessário informar entro do método o que vc quer executar
# print(cursor.fetchall())  # fetchall executa todas as respostas encontradas da query
# query1 = 'SELECT * FROM tb_vendas_dsa'
# cursor.execute(query1)
# nome_colunas = [description[0] for description in cursor.description]
# dados = cursor.fetchall()
# print(dados)
# print(nome_colunas)
# query2 = 'SELECT AVG (Unidades_Vendidas) FROM tb_vendas_dsa'
# cursor.execute(query2)
# print(cursor.fetchall())
query4 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
         FROM tb_vendas_dsa
         WHERE Valor_Unitario > 199
         GROUP BY Nome_Produto'''
cursor.execute(query4)
print(cursor.fetchall())
conexao.close()

