# arquivo = open('primeiro_arquivo.txt', 'w+')


def cadastroArquivo(txt):
    leitura = open('primeiro_arquivo.txt', 'a')
    leitura.write(txt)
    leitura.write('\n')
    leitura.close()

# cadastroArquivo('teste')

def lerArquivo():
    leitura = open('primeiro_arquivo.txt', 'rt')
    for line in leitura:
        print(line)


while True:
    resposta = int(input('Você deseja: 1- Ler arquivo , 2 - Cadastrar Usuário ou 3 - Sair do sistema: '))
    if resposta == 1:
        lerArquivo()
    if resposta == 2:
        adicao = str(input('O que deseja adicionar? '))
        cadastroArquivo(adicao)
    if resposta == 3:
        break
