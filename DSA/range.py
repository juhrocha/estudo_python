#USO DO RANGE PULANDO X CASAS
for item in range(1, 100, 2):
   print(item)

#USO DO RANGE SEM PULAR CASAS
print(f'Início da contagem:')
for valor in range(0, 26):
    print(f'{valor}', end=' ')
print(f'\nFim da contagem')

#RANGE EM LISTAS
list = ['uva', 'maça', 'banana', 'melancia', 'kiwi']
list_tamanho = len(list)
for item in range(0, list_tamanho): #há a possibilidade de adc um intervalo nos "pulos"
    print(list[item])


#ADC NÚMEROS EM UMA LISTA USANDO RANGE
numeros = []
for numero in range(0,51):
    numeros.append(numero)
print(numeros)


#ADC INPUTS NUMA LISTA
nomes = []
for pessoa in range (0,5):
    pessoas = str(input('Qual o seu nome? '))
    nomes.append(pessoas)
print(nomes)
