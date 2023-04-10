# Nesse primeiro exemplo numa segunda tentativa em que o usuário erre, o except não 'funciona'
# try:
#     num1 = int(input('Digite um número inteiro: '))
#     num2 = int(input('Digite outro número inteiro: '))
# except (ValueError, TypeError):
#     novamente = int(input('Você não digitou um número inteiro. Tente novamente: '))
# finally:
#     print('Obrigada pela correção.')

# Já nesse exemplo, o usuário fica preso no looping até acertar o tipo solicitado
def antiuser(mensagem):
    resposta = ''
    while True:
        try:
            resposta = int(input(mensagem))
        except (TypeError, ValueError):
            print('Você não digitou um tipo válido')
            continue
        else:
            break
    return print(f'Você digitou o número {resposta}')


antiuser('Digite um número: ')
