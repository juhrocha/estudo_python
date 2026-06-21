class MinhaClasse:
    def __init__(self):
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'Olá {self.nome}, você tem {self.idade} anos.'
