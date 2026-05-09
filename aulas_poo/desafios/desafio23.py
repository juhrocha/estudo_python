from abc import ABC, abstractmethod

class Poligono (ABC):
    def __init__(self, qtd_lados = 0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, qtd_lados, lado = 0):
        super().__init__(qtd_lados)
        self.lado = lado

    def perimetro(self):
        medida = self.lado * self.qtd_lados
        print(f'O perímetro deste quadrado é de: {medida}')

    def area(self):
        total = self.lado ** 2
        print(f'A área deste quadrado é de: {total}')

class Circulo(Poligono):
    def __init__(self, qtd_lados, raio = 0):
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self):
        medida = self.raio * (2 * 3.14)
        print(f'O perímetro deste círculo é de: {medida:.2f}')

    def area(self):
        total = 3.14 * (self.raio * self.raio)
        print(f'A área deste círculo é de: {total:.2f}')

q1 = Quadrado(4,2)
q1.perimetro()
q1.area()

c1 = Circulo(0, 12) #Considerado 0 lados para o círculo
c1.perimetro()
c1.area()
