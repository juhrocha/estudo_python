from abc import abstractmethod, ABC

class Funcionario(ABC):
    def __init__(self, nome = ''):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.sal_min = 1612
        self.inss = 0.075

    @abstractmethod
    def calc_sal(self):
        pass

    @abstractmethod
    def analisar_sal(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.qtd_horas

    def analisar_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss)
        analise = self.salario / self.sal_min

        print(f'O salário líquido de {self.nome} é de R$ {self.salario:.2f} e corresponde a {analise:.1f} salários mínimos')

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.sal_bruto= salario_bruto

    def calc_sal(self):
        pass

    def analisar_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss)
        analise = self.salario / self.sal_min

        print(f'O salário líquido de {self.nome} é de R$ {self.salario:.2f} e corresponde a {analise:.1f} salários mínimos')

