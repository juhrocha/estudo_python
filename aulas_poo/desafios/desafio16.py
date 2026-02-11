import rich

class Funcionario:
    """Classe que informa o nome do funcionário, qual setor trabalha e o seu cargo atual na empresa Curso em Vídeo"""

    empresa = 'Curso em Vídeo'

    def __init__(self, nome = '', cargo = '', setor = ''):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor


    def apresentacao(self):
        return rich.print(f":writing_hand:  Olá, sou [yellow]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {self.__class__.empresa}")

f1 = Funcionario('Juliana', 'Analista de BI', 'Operações')
f2 = Funcionario('Reinaldo', 'Desenvolvedor Jr.', 'Programação')

print(f1.apresentacao())
print(f2.apresentacao())




