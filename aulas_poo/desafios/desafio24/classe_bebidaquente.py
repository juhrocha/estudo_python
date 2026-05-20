from abc import abstractmethod, ABC

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def ferver_agua(self):
        print('1- Fervendo a água a 100ºC.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def preparar(self):
        #É possível chamar tanto métodos quanto atríbutos com self
        print('INICIANDO O PREPARO')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('BEBIDA PRONTA\n')

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print('2- Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print('3- Servindo em uma xícara pequena.')


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('2- Mergulhando o sachê de ervas na água.')

    def servir(self):
        print('3- Servindo em uma caneca de porcelana com limão.')


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('2- Passando vapor pressurizado pelo bico do leite.')

    def servir(self):
        print('3- Servindo em uma caneca grande, já com café.')