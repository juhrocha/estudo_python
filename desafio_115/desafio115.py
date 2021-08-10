def linha():
    print('~'*30)


def titulo(msg):
    linha()
    print(msg.center(30))
    linha()


def leiaInt(mensagem):
    numero = ''
    try:
        numero = int(input(mensagem))
    except (TypeError, ValueError):
        print('OPÇÃO INVÁLIDA: por favor digite um número inteiro válido!')
    except(KeyboardInterrupt):
        return 0
    else:
        return numero


def menu(lista):
    titulo('MENU PRINCIPAL')
    # print(lista)
    contador = 1 # usando o for, não foi possível usar "count" e "item" então fazer o contador fora e a cada novo laço
    # adc +1 a lista do contador, dessa forma é possível executar o meu dessa forma
    for item in lista:
        print(f'{contador}- {item}')
        contador += 1
    linha()
    opcao = leiaInt('Sua Opção: ')
    return opcao




