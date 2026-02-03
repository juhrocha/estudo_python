from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect
from rich.traceback import install
install()

# python -m rich.emoji : acessa a biblioteca de emojis no rich

print('Olá [red]mundo[/]! :earth_americas:')
print('Meu nome é [bold yellow on black]Juliana[/] :comet:')

caixa = Panel('Aqui é um painel de exemplo :growing_heart:')
print(caixa)

tabela = Table(title='Tabela de preços')
tabela.add_column('Nome', justify= 'center', style='black')
tabela.add_column('Preço', justify= 'right', style='black')
tabela.add_row('Lapís', '1,50' )
tabela.add_row('Caderno', '9,50' )
print(tabela)

inspect(tuple)


def divisao (x, y):
    return x / y

print(divisao(1,0))


