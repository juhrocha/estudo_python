#Solução Juliana
class Produto:
    """Classe que cadastra produto e cria uma etiqueta"""
    def __init__(self, produto = '', preco = 0):
        self.produto = produto
        self.preco = f'R$ {preco:.2f}'

    def etiqueta(self):
        print('-'*23)
        etiqueta = f'Produto:\n******{self.produto}******\nPreço: {self.preco}'
        print(f'{etiqueta:^60}')
        print('-'*23)


p1 = Produto('Celular', 10000)
p2 = Produto('Televisão', 8000)
print(p1.etiqueta())
print(p2.etiqueta())


#Solução CeV
from rich import print
from rich.panel import Panel
class Produto1:
    """Classe que cadastra produto e cria uma etiqueta"""
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def __str__(self):
        return f'{self.produto} custa {self.preco:.2f}'

    def etiqueta(self):
        conteudo = f'{self.produto.center(35, ' ')}'
        precof = f'R${self.preco:.2f}'
        conteudo += f'{precof.center(35, '-')}'
        etiqueta = Panel(conteudo, title='Produto', width=40)
        print(etiqueta)


p3 = Produto1('iPhone 17 Pro Max', 25000.85)
print(p3.etiqueta())