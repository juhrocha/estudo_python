from desafio_115 import desafio115
from time import sleep
from desafio_115 import arquivo

arq = '/home/juliana/Project/estudo_python/desafio_115/arquivo/exercicio_115b.txt'
# arq = 'testanto.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    sleep(1)
    resposta = desafio115.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        desafio115.linha()
        sleep(1)
        desafio115.titulo('OPÇÃO 1')
        arquivo.abreArquivo(arq)
        continue
    if resposta == 2:
        sleep(1)
        desafio115.linha()
        desafio115.titulo('OPÇÃO 2')
        dado = str(input('Digite os dados: '))
        arquivo.cadastroArquivo(arq, dado)
        continue
    if resposta == 3:
        sleep(0.75)
        print('Saindo...Volte sempre!')
        break
    else:
        sleep(0.75)
        desafio115.linha()
        desafio115.titulo('OPÇÃO INVÁLIDA! Digite um número válido.')
