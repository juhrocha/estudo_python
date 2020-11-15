#Exercício 46 - Curso em vídeo
from time import sleep
for fogos in range (10,-1,-1):
    print(fogos)
    sleep(1)
print('BOOM! POW! FELIZ ANO NOVO!')

#Exercício 47 - Curso em vídeo
for par in range (0,50,2):
    print (par+2, end=' ')

# Outra alternativa:
for par in range (2,51,2):
    print (par, end=' ')

#Exercício 48 - Curso em vídeo
soma=0
contador=0
for tres in range (1, 501,2):
    if tres % 3 == 0:
        contador=contador+1
        soma+=tres
print('A soma de todos os {} valores solicitados é igual a {}'.format(contador,soma))


#Exercício 49 - Curso em vídeo
multiplicacao=0
tabuada=int(input('Digite o número que deseja saber a tabuada: '))
for numero in range (1,11):
    multiplicacao=tabuada*numero
    print('{} x {} = {}'.format(tabuada, numero, multiplicacao))

#Exercício 50 - Curso em vídeo
soma=0
contador=0
for par in range (1,7):
    numero=int(input('Digite um valor: '))
    if numero %2 == 0:
        soma+=numero
        contador+=1
print('A soma de {} números pares é igual a: {}'.format(contador, soma))