#Exercício 66 - Curso em vídeo
soma = contador = 0
while True:
    numero=int(input('Digite um número [Ou digite 999 para parar]: '))
    if numero == 999:
        break
    soma+=numero
    contador+=1
print(f'Foram digitados {contador} e a soma desses é igual a {soma}')

#Exercício 67 - Curso em vídeo
from time import sleep
numero = contador = 0
while True:
    numero=int(input('Digite o número que deseja saber a tabuada: '))
    if numero <:
        break
    sleep(1)
    print('*'*11)
    for tabuada in range (1,11):
        print(f'{numero} x {tabuada} = {numero*tabuada}')
    print('*'*11)
print('FIM')

#Exercício 68 - Curso em vídeo
import random
vitoria=0
while True:
    jogador=int(input('Diga um valor: '))
    computador=random.randint(0,10)
    total = jogador + computador
    jogo = ''
    jogo=str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    if jogo == 'P':
        if total % 2 == 0:
            print('GANHOU!')
            vitoria+=1
        else:
            print('ERROU!')
            break
    elif jogo == 'I':
        if total % 2 != 0:
            print('GANHOU!')
            vitoria+=1
        else:
            print('ERROU!')
            break
    else:
        jogo=str(input('TENTE NOVAMENTE: Par ou ímpar? [P/I]: ')).upper().strip()[0]
print(f'Você teve um total de {vitoria} vitória (s)')          
    
#Exercício 69 - Curso em vídeo
maioridade = contador_homem = contador_mulher = 0
while True:
    idade=int(input('Qual sua idade? '))
    sexo=str(input('Qual seu sexo? [M/F]? ')).upper().strip()[0]
    continuar=str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        maioridade+=1
    if sexo == 'M':
        contador_homem+=1
    if sexo == 'F' and idade < 20:
        contador_mulher+=1
    if continuar == 'N':
        break
print(f'''Neste grupo temos:
{maioridade} pessoas maiores de idade;
{contador_homem} são homens;
{contador_mulher} são mulheres com menos de 20 anos.''')
print('FIM')