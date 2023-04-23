class Circulo:
  pi = 3.14

  def __init__(self, raio = 5):
    self.raio = raio

  def area(self):
    return (self.raio * self.raio) * Circulo.pi

  def getRaio(self):
    return self.raio

  def setRaio(self, novo_raio):
    self.raio = novo_raio
    return 'Registrado'


circulo1 = Circulo()
print(circulo1.area())
"""Devido alguns tipos de métodos e atributos o mais indicado é criar métodos dentro da classe que sejam capazes de 
trazer o get e set, ao invés de usá-los no decorrer do código. Um tipo privado, por ex., não funcionaria desse modo"""
print(getattr(circulo1, 'raio'))

