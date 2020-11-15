for repeticao in range (0,10):
    print('Olá, me chamo Juliana!')

for numero in range (0,15):
    print(numero+1)

for pulo in range (0,10,2):
    print (pulo)

for contrario in range (10,0,-1):
    print (contrario)

inicio=int(input('Digite o início: '))
fim=int(input('Digite o fim: '))
pulo=int(input('Digite o número de casas que quer pular: '))
for contador in range (inicio, fim+1, pulo):
    print(contador)


soma = 0
for soma1 in range (0,3):
    numero=int(input('Digite um número: '))
    soma = soma + numero
    #Também pode ser: soma+=numero
print('A soma de todos esses números é igual a {}'.format (soma))

