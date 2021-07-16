# Exercício 101 - Curso em Vídeo - 1ª tentativa
# from datetime import date
def voto (ano=0):
    eleicao = date.today().year - ano
    if eleicao >=18 and eleicao <= 70:
        print('VOTO OBRIGATÓRIO')
    elif eleicao < 16:
        print('NÃO VOTA')
    elif eleicao >= 16 and eleicao > 70:
        print('VOTO OPCIONAL')


ano_nascimento = int(input('Digite o ano de nascimento: '))
voto(ano_nascimento)

# Exercício 101 - Curso em Vídeo - 2ª tentativa
from datetime import date


def voto(ano=0):
    idade = date.today().year - ano
    if idade < 16:
        return print(f'NÃO VOTA')
    elif 16 >= idade < 18 or idade >= 70:
        return print(f'VOTO OPCIONAL')
    else:
        return print(f'VOTO OBRIGATÓRIO')


ano_nascimento = int(input('Digite o ano de nascimento: '))
voto(ano_nascimento)


# Exercício 102 - Curso em Vídeo
def fatorial(numero, show=False):
    """
    Programa retorna o fatorial do número indicado
    :param numero: valor que deve ser indicado, no qual deseja-se saber o fatorial
    :param show: parâmetro opcional, em caso de True exibirá o cálculo do fatorial,
    em caso de False apenas exibirá o resultado
    :return: retorna o resultado do cálculo
    """
    factorial = 1
    for count in range(numero, 0, -1):
        factorial *= count
        if show:
            print(f'{count}', end=' ')
            if count > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
    return print(factorial)


fatorial(5, True)
fatorial(10, True)
fatorial(4)
help(fatorial)

# Exercício 103 - Curso em Vídeo
def ficha (jogador='<desconhecido>', gol=0):
    if jogador == '':
        jogador = 'desconhecido'
    if gol == '':
        gol = 0
    return print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


nome_jogador = input('Nome do jogador: ')
num_gols = input('Número de gols: ')
ficha(nome_jogador, num_gols)
