from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia = 0):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        frete = self.fator * self.distancia
        print(f'O valor da entrega por meio da Moto será de R${frete:.2f}')


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        frete = self.fator * self.distancia
        if self.distancia < 50:
            print('A distância mínima para entregas via Caminhão é de 50km, por favor busque outra alternativa.')
        else:
            print(f'O valor da entrega por meio do Caminhão será de R${frete:.2f}')

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self):
        frete = self.fator * self.distancia
        if self.distancia > 10:
            print('A distância máxima para entregas via Drone é de 10km, por favor busque outra alternativa.')
        else:
            print(f'O valor da entrega por meio do Drone será de R${frete:.2f}')
