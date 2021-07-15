# Exercício 101 - Curso em Vídeo
from datetime import date
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

# Exercício 102 - Curso em Vídeo
