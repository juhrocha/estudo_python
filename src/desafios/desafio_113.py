# Exercício 113 - Curso em vídeo
# def leiaFloat(mensagem):
#     real = ''
#     try:
#         real = float(input(mensagem))
#     except (TypeError, ValueError):
#         print('Erro: por favor digite um número real válido!')
#         return leiaFloat(mensagem)
#     else:
#         return real


def leiaInt(mensagem):
    numero = ''
    try:
        numero = int(input(mensagem))
    except (TypeError, ValueError):
        print('Erro: por favor digite um número inteiro válido!')
#        return leiaInt(mensagem)
    else:
        return numero


# inteiro = leiaInt('Digite um número inteiro: ')
# real = leiaFloat('Digite um número real: ')
# print(f'O número inteiro digitado foi {inteiro} e o número real digitado foi {real}')


# Exercício 114 - Curso em vídeo
# import urllib.request
# try:
#     site = urllib.request.urlopen('http://pudim.com.br/')
# except urllib.error.URLError:
#     print('Site Indisponível')
# else:
#     print('Site Disponível')
