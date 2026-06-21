from abc import abstractmethod, ABC

class Funcionario(ABC):
    # Atributos simples, sem uso de self
    salario_min = 1612
    inss = 0.075

    def __init__(self, nome = ''):

        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

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
        self.salario_bruto = self.valor_hora * self.qtd_horas

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss)

    def analisar_sal(self):
        analise = self.salario / Funcionario.salario_min

        print(f'O salário líquido de {self.nome} é de R$ {self.salario:.2f} e corresponde a {analise:.1f} salários mínimos')

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto = Funcionario.salario_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss)

    def analisar_sal(self):
        analise = self.salario / Funcionario.salario_min

        print(f'O salário líquido de {self.nome} é de R$ {self.salario:.2f} e corresponde a {analise:.1f} salários mínimos')