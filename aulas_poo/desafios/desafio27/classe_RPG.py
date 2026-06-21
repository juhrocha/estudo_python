# Código feito junto ao Guanabara

from abc import ABC, abstractmethod
from random import randint, randrange

class Personagem(ABC):
    golpes = 0

    def __init__(self, nome = '', vida = 0):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 10):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange (0, len(self.golpes))]
            print(f'{self.nome} atacou {alvo.nome} com o {golpe}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque de {self.nome} -> {alvo.nome} não pode ocorrer!')


    def receber_dano(self, valor_dano):
        potencia_golpe = randint(0, valor_dano)
        self.vida = self.vida - potencia_golpe
        if self.vida < 0:
            self.vida = 0
        print(f'O {self.nome} recebeu dano de {potencia_golpe}!')

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Kame-hame-haa', 'Meteoro de Pegasus', 'Espada Gelo']

    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        print(f'O guerreiro {self.nome} conseguiu {cura} pontos de cura')


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Magia das Sombras', 'Magia de Raio', 'Magia do Fogo']

    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        print(f'O mago {self.nome} fez uma magia de cura e conseguiu {cura} pontos de cura')

