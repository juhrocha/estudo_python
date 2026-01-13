# Exercício 88 - Curso em vídeo
from random import randint
jogo_mega = [] # Lista que abrigará todos os dados
jogos = [] # Sublista que abrigará os números do sorteio
contador = 0 # Contador da quantidade de números do jogo. Na mega o máximo de números do jogo é 6
total_sorteio = 1 # Total de sorteios, que se inicia em 1 (1 jogo é o mínimo)
sorteio = int(input('Quantos sorterios você quer fazer? '))
while total_sorteio <= sorteio: # Enquanto o total_sorteio for menor ou igual ao número inputado o programa rodará
    contador = 0 # Ainda nao ha qtd de jogos no inicio do laço
    while True: # Um novo laço para adc numeros a lista de maneira que nao se repitam
        numero = randint(1, 60) # numeros de 1 a 60 e aleatorios
        if numero not in jogo_mega: # if para adc numeros a lista caso nao se repitam
            jogo_mega.append(numero)
        contador += 1 # incremento "uma passada" do laço
        if contador >= 6: # qdo o laço for maior ou igual a 6 deve parar
            break
    jogo_mega.sort() # coloco em ordem os numeros da lista
    jogos.append(jogo_mega[:]) # e crio uma copia da lista principal na sublista
    jogo_mega.clear() # limpo a primeira lista para facilitar a exibiçao
    total_sorteio += 1 # incremento uma passada do laço no total_sorteios
print(f'Os números da sorte são: {jogos}')

# Exercício 89 - Curso em vídeo
alunos = []
while True: # Aqui solicito ao usuário as infos e questiono se deseja continuar,
    #  e append a info já recebida no input usando o nome da váriavel
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1+nota2)/2
    alunos.append([nome, [nota1, nota2], media]) # nome posição 0, nota 1 e 2 posição 1 e média posição 2
    resposta = str(input('Você deseja continuar: [S/N] ')).upper().strip()
    if resposta == 'N':
        break
for indexador, pessoa in enumerate(alunos): # ennumerate permite usar o indexador
    print(f'Aluno: {indexador}', end=' ')
    print(f'Nome: {pessoa[0]}', end=' ')
    print(f'Média: {pessoa[2]}')
while True:
    estudante = int(input('Você deseja saber as notas de algum aluno? '
                      '[Digite a posição do aluno ou digite 99 para encerrar]: '))
    if estudante == 99:
        break
    if estudante <= len(alunos) -1 : # se estudante receber um valor <= ao tamanho da lista -1 ele exibirá o print
# -1 pq, exemplo: lista [1,2,3], posições [0,1,2] vc quer saber da posição 1, mas no python a posição 1 é 0
        print(f'O aluno {alunos[estudante][0]} tem as notas: {alunos[estudante][1]}')
    if estudante > len(alunos): # se estudante receber um valor maior que a lista será orientado a tentar novamente
        print('POSIÇÃO ERRADA!!, TENTE NOVAMENTE')




