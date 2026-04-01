from rich import print

class Gamer:
    """Classe responsável por criar a ficha dos jogadores de uma unidade"""
    def __init__(self, nome = '', nick = ''):
        self.nome = nome
        self.nick = nick
        self.lista_jogos = []

    def add_favoritos(self, jogo = ''):
        self.lista_jogos.append(jogo)

    def ficha (self):
        print(f':joystick: Jogador: [red]{self.nick}[/]')
        print(f'Nome real: {self.nome}')
        print(f':video_game: Jogos favoritos: \n{'\n'.join(sorted(self.lista_jogos))}')

        """a função join serve para juntar strings com um separador determinado pelo usuário
        Utilização: ~separador~.join(string)
        Exemplo: lista = ["LOL", "Ragnarok", "CS"]
        print(", ".join(lista))"""

j1 = Gamer('Juliana', 'ju-3')
j1.add_favoritos('Ragnarok')
j1.add_favoritos('LOL')
j1.add_favoritos('Mario Bros')
j1.add_favoritos('Street Fighter')
j1.ficha()




