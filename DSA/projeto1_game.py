# SEGUINDO PASSO A PASSO DO CHAT GPT + PERSONALIZAÇÃO
from DSA import projeto1_game_v2
from time import sleep
print('Bem vinde ao jogo de forca!')
sleep(0.5)
print('Vamos comerçar!')

# PASSO 1
palavras = ['banana', 'cinema', 'musica', 'televisao', 'computador']

# PASSO 2
from random import choice
palavra_aleatoria = choice(palavras)
# print(palavra_aleatoria)

# PASSO 3
tracos = '_' * len(palavra_aleatoria)
letras_descobertas = []
letras_erradas = []

# PASSO 4 a 7
tamanho = len(palavra_aleatoria)
tentativa = 0
sleep(0.5)
while True:
    print(f'Palavra: {tracos}')
    letra = str(input('Adivinhe uma letra da palavra: ')).strip().lower()
    if letra in palavra_aleatoria:
        print('Acertou!')
        letras_descobertas.append(letra)
        for indexador in range(len(palavra_aleatoria)):
            if palavra_aleatoria[indexador] == letra:
                tracos = tracos[:indexador] + letra + tracos[indexador+1:]
        tentativa += 1
    else:
        print('Você errou!')
        letras_erradas.append(letra)
        print(f'Tentativas: {letras_erradas}')
        projeto1_game_v2.display_forca(tentativa)
        tentativa += 1
    if tracos == palavra_aleatoria:
        print(f'Você adivinhou a palavra: {palavra_aleatoria}')
        break
    elif tentativa >= tamanho:
        print('Você foi enforcado!')
        break

sleep(0.5)
print('FIM DE JOGO')

