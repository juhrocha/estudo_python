class Musica:
    def __init__(self, musica, banda):
        self.musica = musica
        self.banda = banda

    def ouvindo(self):
        pass


class Rock(Musica):

    def ouvindo(self):
        print(f'Eu estou ouvindo {self.musica}, da banda {self.banda}')


musica1 = Rock('Edge of Seventeen', 'Stevie Nicks')
musica1.ouvindo()

