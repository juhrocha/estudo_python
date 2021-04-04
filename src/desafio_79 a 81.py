#Exercício 79 - Curso em vídeo
aleatorio=[]
while True:
   numero=(int(input('Digite um número: ')))
   if numero not in aleatorio:
       aleatorio.append(numero)
   else:
       print('Valor duplicado! Não adicionado a lista')
   resposta=str(input('Você deseja continuar? [S/N]: ')).upper().strip()
   if resposta == 'N':
       break
aleatorio.sort()
print(aleatorio)

#Exerício 80 - Curso em vídeo
lista=[]
for count in range (0,5):
   numero=(int(input('Digite um valor: '))) # Aqui eu ainda não devo inserir o .append
#Se count = 0 (ou seja é a primeira vez do laço) ou o número é maior que o último da lista, eu uso o .append, pois o
# .append adiciona coisas ao final da lista
   if count == 0 or numero > lista[-1]:
       lista.append(numero)
#Aqui é a execução do "meio" da lista"
   else:
#Determino uma posição inicial (ou seja 0) e crio um laço onde: enquanto o número for o menor ele será adicionado a
# #posição 0 da lista, caso seja seja o segundo menor será adicionado mais uma posição
       posicao=0
       while posicao < len(lista):
           if numero <= lista[posicao]:
              lista.insert(posicao,numero)
               break
           posicao+=1
print(lista)

#Exerício 81 - Curso em vídeo
numeral=[]
while True:
    numeral.append(int(input('Digite um número: ')))
    answer=str(input('Você deseja continuar? [S/N]: ')).upper().strip()
    if answer == 'N':
        break
print(f'Os números digitados foram: {numeral}')
print(f'Tivemos um total de {len(numeral)} números digitados')
numeral.sort(reverse=True)
print(f'A lista em ordem decrescente é {numeral}')
if 5 in numeral:
    print(f'O número 5 está na posição {numeral.index(5)+1} dessa lista')
else:
    print('Não há o número 5 nessa lista')
