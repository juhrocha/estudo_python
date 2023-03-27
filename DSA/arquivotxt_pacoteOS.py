#texto = 'Essa sou eu estudando Python \n'
#texto = texto + 'junto a DSA \n'
#texto += 'enquanto escuto música'
#print(texto)
#
# import os
# arquivo = open(os.path.join('/home/juliana/Documentos/teste.txt'),'w')
# for palavra in texto.split():
#     arquivo.write(palavra + ' ')
# arquivo.close()
#
# arquivo = open(os.path.join('/home/juliana/Documentos/teste.txt'),'r')
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

#USANDO WITH
# with open('/home/juliana/Documentos/teste.txt', 'w') as arquivo:
#     arquivo.write(texto[:19])
#     arquivo.write('\n')
#     arquivo.write(texto[23:30])
#
# with open('/home/juliana/Documentos/teste.txt', 'r') as arquivo1:
#     conteudo = arquivo1.read()
#     print(conteudo)

with open('/home/juliana/Documentos/teste.txt', 'w') as arquivo:
    arquivo.write('\ntestando 1 2 3')

arquivo1 = open('/home/juliana/Documentos/teste.txt', 'r')
conteudo = arquivo1.read()
arquivo1.close()
print(conteudo)



