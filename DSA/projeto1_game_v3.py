from random import choice
from time import sleep
from DSA import projeto1_game_v2
palavras = ['musica', 'garrafa', 'adesivos', 'teclado', 'celular']
palavra_escolhida = choice(palavras)


def inicio():
    print('Bem vinde ao jogo de forca!')
    sleep(0.5)
    print('Vamos comerçar!')


def final():
    palavras.clear()
    sleep(0.5)
    print('FIM DE JOGO')


class JogoForca:
    def __init__(self):
        self.palavra = palavra_escolhida
        self.tracos = '-' * len(palavra_escolhida)
        self.ldescoberta = []
        self.lerrada = []
        self.tamanho = len(palavra_escolhida)
        self.tentativa = 0
        inicio()

    def adivinhacao(self):
        while True:
            print(f'Palavra: {self.tracos}')
            letra = str(input('Adivinhe uma letra da palavra: ')).strip().lower()
            if letra in self.palavra:
                print('Acertou!')
                self.ldescoberta.append(letra)
                for indexador in range(len(self.palavra)):
                    if self.palavra[indexador] == letra:
                        self.tracos = self.tracos[:indexador] + letra + self.tracos[indexador + 1:]
                self.tentativa += 1
            else:
                print('Você errou!')
                self.lerrada.append(letra)
                print(f'Tentativas: {self.lerrada}')
                projeto1_game_v2.display_forca(self.tentativa)
                self.tentativa += 1
            if self.tracos == self.palavra:
                print(f'Você adivinhou a palavra: {self.palavra}')
                break
            elif self.tentativa >= self.tamanho:
                print('Tentativas excedidas! Você foi enforcado!')
                break
        final()


jogar = JogoForca()
jogar.adivinhacao()
