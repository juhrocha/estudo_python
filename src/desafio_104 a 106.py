# Exercício 104 - Curso em vídeo - Pedir ajuda
def leiaInt(mensagem):
    flag = False
#    valor = input(mensagem)
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            return print(f'Você digitou o número {valor}')
            flag = True
        else:
            print(f'ERRO! Digite um número inteiro')
            return leiaInt(mensagem)
        if flag:
            break


valor = leiaInt('Digite um número: ')

# Exercício 105 - Curso em vídeo
# def notas(*notas, situacao=False):
#     """
#     Programa recebe dois paramêtros: número de notas e situação do aluno
#     :param notas: parâmetro obrigatório, porém indefinido. Recebe a quantidade de notas do aluno
#     :param situacao: parâmetro opcional. Recebe a situação do aluno de acordo com sua média
#     :return: retorna um dicionário que contém: o total de notas, a maior e a menor nota, a média das notas informadas e
#     a situação do aluno, caso o usuário opte por sua exibição
#     """
#     avaliacao_aluno = {'total de notas': len(notas), 'maior': max(notas), 'menor': min(notas)}
#     from statistics import mean
#     avaliacao_aluno['média'] = mean(notas)
#     if situacao is True:
#         avaliacao_aluno['situação'] = ''
#         if avaliacao_aluno['média'] < 5:
#             avaliacao_aluno['situação'] = 'Reprovado'
#         elif avaliacao_aluno['média'] > 6:
#             avaliacao_aluno['situação'] = 'Aprovado'
#         else:
#             avaliacao_aluno['situação'] = 'Recuperação'
#     print(avaliacao_aluno)
#
#
# notas(10, 7, 0, situacao=True)
# notas(5, 6, 7.5)
# # help(notas)

# # Exercício 106 - Curso em vídeo - Melhorar
# def encerramento():
#     print('\033[44m *' * 9)
#     print(f'\033[44m Até Logo!')
#     print('\033[44m *' * 9)
#
#
# def sistema():
#     print('\033[45m * ' * 9)
#     print('\033[45m Sistema de ajuda PyHelp')
#     print('\033[45m * ' * 9)
#     print('\033[m')
#
#
# def ajuda(mensagem):
#     flag = False
#     sistema()
#     ajudar = input(mensagem)
#     while True:
#         if ajudar in 'fim':
#             flag = True
#             break
#         print(f'{help(ajudar)}')
#         return ajuda(mensagem)
#     return encerramento()
#
#
# print(ajuda('Função ou Biblioteca > '))


