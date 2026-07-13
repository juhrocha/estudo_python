class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 16 <= valor <= 30:
            if valor % 0.5 == 0:
                self.__temperatura = valor
            else:
                print('Temperatura inválida!')
        else:
            print('Temperatura inválida!')

    @property #alteração Guanabara, posso usar N properties
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'