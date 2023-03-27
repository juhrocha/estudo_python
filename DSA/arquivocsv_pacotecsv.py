#USANDO PACOTE CSV
import csv
#with open('/home/juliana/Documentos/testecsv.csv', 'r') as arquivo:
#    conteudo = arquivo.read()
#    print(conteudo)

#USANDO CSV PARA INSERIR INFORMAÇÕES NAS LINHAS
# with open('/home/juliana/Documentos/testecsv.csv', 'w') as gravacao:
#     gravar = csv.writer(gravacao)
#     gravar.writerow(('numero', 'numero1', 'numero2'))
#     gravar.writerow((1, 2, 3))
#     gravar.writerow((4, 5, 6))
#
# with open('/home/juliana/Documentos/testecsv.csv', 'r') as arquivo1:
#     planilha = arquivo1.read()
#     print(planilha)

#USANDO PANDA PARA A EXIBIÇÃO DO ARQUIVO JÁ ALTERADO
import pandas
data = pandas.read_csv('/home/juliana/Documentos/testecsv.csv')
print(data)
