class Musica:
    def __init__(self):
        self.musica = 'Black Summer'
        self.banda = 'RHCP'

    def ouvindo(self):
        pass


class Rock(Musica):
    def __init__(self):
        Musica.__init__(self)
        pass

    def ouvindo(self):
        return f'Eu estou ouvindo {self.musica}, da banda {self.banda}'


music = Rock()
print(music.ouvindo())

