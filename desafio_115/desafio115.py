#revisar
from time import sleep
from src import desafio_113


def linha():
    print('~' * 30)


def titulo(mensagem):
    print(mensagem.center(30))


def menu(list):
    sleep(0.5)
    linha()
    titulo('MENU PRINCIPAL')
    linha()
    sleep(1)
    count = 1
    for item in list:
        print(f'{count}- {item}')
        count += 1
    linha()
    sleep(1)
    opcao = desafio_113.leiaInt('Sua opção: ')
    sleep(1)
    return opcao

