# Resolução com Guanabara, não pensei em soluções além de traduzir cor por cor. O que não é o ideal.
# No final ele traduziu as cores
from rich import  print

class Caneta:
    """Classe responsável por escrever com a cor selecionada pelo usuário"""

    def __init__(self, cor = 'azul'):
        escolha = ''
        """match aqui funciona quase como um if else"""
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case 'amarelo':
                escolha = '[yellow]'
            case _:
                escolha = '[white]'
        self.cor = escolha

    def escrever (self, texto):
        print(f'{self.cor}{texto}[/]')

c1 = Caneta('verde')
c1.escrever('Nossa, como o dia hoje está bonito!')
