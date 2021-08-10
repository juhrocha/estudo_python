from desafio_115 import desafio115
from time import sleep
# from desafio_115 import arquivo
#
# arqv = 'cursoemvideo.txt'
#
# if arquivo.arquivoExiste(arqv):
#     print('Arquivo encontrado com sucesso!')
# else:
#     print('Arquivo não encontrado')

while True:
    sleep(0.75)
    resposta = desafio115.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        desafio115.linha()
        sleep(0.75)
        desafio115.titulo('OPÇÃO 1')
        continue
    if resposta == 2:
        sleep(0.75)
        desafio115.linha()
        desafio115.titulo('OPÇÃO 2')
        continue
    if resposta == 3:
        sleep(0.5)
        print('Saindo...Volte sempre!')
        break
    else:
        sleep(0.75)
        desafio115.linha()
        desafio115.titulo('OPÇÃO INVÁLIDA! Digite um número válido.')

