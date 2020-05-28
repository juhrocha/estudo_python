numero=float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(numero, int(numero)))


catetoo=float(input('Comprimento do cateto oposto: '))
catetoa=float(input('Comprimento do cateto adjacente: '))
hipotenusa=((catetoo **2 + catetoa **2) ** (1/2))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

catetoo=float(input('Comprimento do cateto oposto: '))
catetoa=float(input('Comprimento do cateto adjacente: '))
import math 
hipotenusa=math.hypot(catetoo, catetoa)
print('A hipotenusa é igual a: {:.2f}'.format(hipotenusa))

from math import sin,cos,tan,radians
angulo=float(input('Digite o angulo que voce deseja: '))
seno=sin(radians(angulo))
coseno=cos(radians(angulo))
tangente=tan(radians(angulo))
print('Para o angulo {:.2f} o seno e {:.2f}, o coseno e {:.2f} e a tangente e {:.2f}'.format(angulo,seno,coseno,tangente))




















