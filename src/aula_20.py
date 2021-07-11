def mostra_linha():
   print('*' * 30)


mostra_linha()
print('Olá mundo')
mostra_linha()

def linhas(txt):
   print('*'*30)
   print(txt)
   print('*'*30)


linhas('Meu nome é Juliana')

def soma(a, b, c):
   print(a + b + c)

soma(1, 2, 3)
soma(7, 0, 3)
soma(1, 2, 10)

def contador(*num):
   from time import sleep
   for valor in num:
       print(f'{valor} ',end=' ')
       sleep(0.5)
   print('FIM!')


contador(1, 2, 3, 4, 5, 6, 5, 9, 0)
contador(1, 2, 3)
contador(0)

valores=[2, 3, 4, 5]
def dobro(list):
    posicao = 0
    while posicao < len(list):
       list[posicao]*=2
       posicao+=1


dobro(valores)
print(valores)
