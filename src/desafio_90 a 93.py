# Exercício 90 - Curso em vídeo
dados_alunos = {}
dados_alunos['Nome'] = str(input('Digite o nome do aluno: '))
dados_alunos['Media'] = float(input('Digite a média do aluno: '))
if dados_alunos['Media'] == 5:
    dados_alunos['Situacao'] = 'Recuperação'
elif dados_alunos['Media'] > 5:
    dados_alunos['Situacao'] = 'Aprovado'
elif dados_alunos['Media'] < 5:
    dados_alunos['Situacao'] = 'Reprovado'
for key, value in dados_alunos.items():
    print(f'{key} é igual a {value}')

# Exercício 91 - Curso em vídeo
import random, time, operator
sorteio_dado = {'jogador_1': random.randint(1,6),
                'jogador_2': random.randint(1,6),
                'jogador_3': random.randint(1,6),
                'jogador_4': random.randint(1,6)}
ranking = []
print('Os números sorteados foram: ')
for key, value in sorteio_dado.items():
    print(f'{key} teve o número {value} sorteado')
    time.sleep(1)
print('*'*30)
ranking = sorted(sorteio_dado.items(), key=operator.itemgetter(1), reverse=True)
print('*RANKING*')
for item, valor in enumerate (ranking):
    print (f'{item+1}o lugar: {valor[0]} com {valor[1]}')
    time.sleep(1)

# Exercício 92 - Curso em vídeo
import datetime
dados_usuario = {}
dados_usuario['Nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
dados_usuario['Idade'] = datetime.date.today().year - idade
dados_usuario['CTPS'] = int(input('Nº CTPS (Sem doc. informar "0"): '))
if dados_usuario['CTPS'] == 0:
    print('Dados coletados.')
else:
    dados_usuario['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados_usuario['Salário'] = int(input('Salário: R$ '))
    dados_usuario['Aposentadoria'] = (dados_usuario['Idade'] + 35)
print('*'*30)
for key, value in dados_usuario.items():
    print(f'{key} é igual a {value}')

# Exercício 93 - Curso em vídeo
from math import fsum
dados_jogador = {}
gols=[]
dados_jogador['Nome'] = str(input('Nome do jogador: '))
partida = int(input('Quantas partidas ele jogou? '))
for count in range (0, partida):
    gols.append(int(input(f'Quantos gols na partida {count+1}? ')))
dados_jogador['Gols'] = gols[:]
dados_jogador['Total de gols'] = fsum(gols)
print('*'*30)
print(dados_jogador)
print('*'*30)
for key, value in dados_jogador.items():
    print(f'O campo {key} tem o valor de {value}.')
print('*'*30)
print(f'O jogador {dados_jogador["Nome"]} jogou {partida} partida(s).')
for play, gol in enumerate (gols):
    print(f'-> Na partida {play+1}, fez {gol} gol(s).')
print(f'Sendo um total de {dados_jogador["Total de gols"]} gols')
