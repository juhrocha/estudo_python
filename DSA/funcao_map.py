#def potencia(x):
#    return pow(x, 2)

#numeros = [1, 2, 3, 4, 5]
#num_quadrado = list(map(potencia, numeros))
#print(num_quadrado)

#Usar map somente em listas (considerar tuplas e dicionários tbm)
#def caixa_alta(txt):
#    return txt.upper()


#texto = str(input('Digite um texto: '))
#resposta = list(map(caixa_alta, texto))
#print(f'Esse é seu texto em caixa alta {resposta}')

#MAP USANDO LAMBDA
from random import randint
list=[]
for x in range(0, 3):
    list.append(randint(1, 90))
print(list)

tupla = tuple(map(lambda numero: numero * 2, list))
print(tupla)
