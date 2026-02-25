from rich import print
class Churrasco:
    """Calcula com base no nº de participantes informados a qtd recomendada de carne e o valor aproximado do evento
        Considerado:
        Consumo de 400g por pessoa
        Valor da carne: R$45,90/kg
    """
    def __init__(self, evento = '', num = 0):
        self.evento = evento
        self.num = num

        kg = 1000
        compra = 0.4 * self.num
        self.kg_churrasco = 0

        if compra < 1000:
            self.kg_churrasco = compra
        else:
            self.kg_churrasco = compra/kg

        vlr_quilo = 45.90
        self.custo = self.kg_churrasco * vlr_quilo

        self.divisao = self.custo/self.num

    def analise(self):
        print('-'*60)
        print(f'{self.evento.center(60, ' ')}')
        print(f'Análise de [yellow]{self.evento}[/] com [yellow]{self.num} participantes[/]')
        print(f'Recomendo comprar [red]{self.kg_churrasco:.3f}kg[/]')
        print(f'O custo total será de [red]R${self.custo:.2f}[/]')
        print(f'Cada pessoa pagará [red]R${self.divisao:.2f}[/]')
        print('-' * 60)


c1 = Churrasco('Níver da Ju', 50)
c2 = Churrasco('FDS dos amigos', 9)
print(c1.analise())
print(c2.analise())