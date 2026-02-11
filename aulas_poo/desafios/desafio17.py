from rich.table import Table

class Produto:
    def __init__(self, produto = '', preco = 0):
        self.produto = produto
        self.preco = f'R$ {preco:.2f}'

    def criar_tabela(self):
        etiqueta = Table(title = 'Produto')
        etiqueta.add_row(self.produto)
        etiqueta.add_row(self.preco)

    def __str__(self):
        print(self.criar_tabela())


p1 = Produto('Celular', 10000)
print(p1.criar_tabela())