#LENDO ARQUIVO ONLINE
#import json
#from urllib.request import urlopen
#resposta = urlopen('https://viacep.com.br/ws/18030305/json/').read().decode('utf8')
#dados = json.loads(resposta)
#print(dados)

#COPIANDO CONTEÚDO
arquivo_fonte = '/home/juliana/Documentos/Documento não-salvo 1.json'
arquivo_destino = '/home/juliana/Documentos/testando.txt'
#with open(arquivo_fonte, 'r') as file:
#    text = file.read()
#    with open(arquivo_destino, 'w') as arquivo:
#        gravar_texto = arquivo.write(text)

with open('/home/juliana/Documentos/testando.txt', 'r') as leitura:
    conteudo = leitura.read()
    print(conteudo)



