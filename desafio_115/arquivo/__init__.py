# Como abrir arquivo e exibir um arquivo para leitura
# a = open('./exercicio_115b.txt', 'rt')
# for line in a:
#     print(line)

arq = '/home/juliana/Project/estudo_python/desafio_115/arquivo/exercicio_115b.txt'


def arquivoExiste(arquivo):
    try:
        leitura = open(arquivo, 'rt')
        leitura.close()
    except:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        leitura = open(arquivo, 'rt')
    except (FileNotFoundError, FileExistsError):
        leitura = open(arquivo, 'wt+')
    else:
        for line in leitura:
            print(line)


# criarArquivo('Juliana.txt')


def abreArquivo(arquivo):
    leitura = open(arquivo, 'rt')
    for line in leitura:
        print(line)


# abreArquivo('exercicio_115b.txt')


def cadastroArquivo(arquivo, txt):
    leitura = open(arquivo, 'a')
    leitura.write(txt)
    leitura.write('\n')
    leitura.close()


# cadastroArquivo('Ju, 24')
