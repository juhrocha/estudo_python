#LEITURA DE ARQUIVO TXT
arquivo = open('/home/juliana/Documentos/teste.txt', 'r') #abre o arquivo para leitura, r = read
print(arquivo.read()) #printa o que está escrito no arquivo
print(arquivo.tell()) #conta a qtd de caracteres
print(arquivo.read()) #após printar o arquivo uma vez, o cursor move para o final do texto.
# no segundo print ele vem em branco
print(arquivo.seek(0, 0)) #retorna o cursor para a posição 0
print(arquivo.read(14)) #exemplo de fatiamento do read, mostrando x qtd de caracteres

#SUBESCREVENDO TEXTO DO ARQUIVO TXT
arquivo1 = open('/home/juliana/Documentos/testando.txt', 'w') #abre o arquivo para edição (subescrevendo), w = write
arquivo1.write('0 -1 -2 -3')
arquivo1.close()
arquivo1 = open('/home/juliana/Documentos/testando.txt', 'r')
print(arquivo1.seek(0, 0))
print(arquivo1.read())

#ACRESCENTANDO TEXTO DO ARQUIVO TXT
arquivo2 = open('/home/juliana/Documentos/3.txt', 'a')
arquivo2.write('5 6 7 8 ')
arquivo2.close()
arquivo2 = open('/home/juliana/Documentos/3.txt', 'r')
print(arquivo2.read())


#LENDO ARQUIVO CSV
planilha = open('/home/juliana/Documentos/testecsv.csv', 'r')
# print(planilha.read().split('\n')) #print do arquivo sendo executado em uma linha

#USANDO PANDAS
import pandas as pd
arquivo = '/home/juliana/Documentos/testecsv.csv'
data = pd.read_csv(arquivo)
print(data)











