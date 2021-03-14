# Exercício 82 - Curso em vídeo
lista_num=[]
par=[]
impar=[]
while True:
    lista_num.append(int(input('Digite um valor: ')))
    resposta=str(input('Você deseja continuar adicionando elementos à lista? [S/N] ')).upper().strip()
    if resposta == 'N':
        break
print(lista_num)
for indice, valor in enumerate(lista_num):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Essa lista contém os números pares: {par}')
print(f'E contém os números ímpares {impar}')

# Exercício 83 - Curso em vídeo
expressao= str(input('Digite uma expressão: ')) #Crio primeiro um input em str, pois string é uma lista que pode ser fatida
lista=[]
for simbolo in expressao: #Crio um for para "pegar" cada símbolo dentro da expressão
    if simbolo == '(':
        lista.append('(') #A cada vez que receber '(' ele será incluso na lista
    elif simbolo == ')': #Ao receber ')' críamos condições:
        if len(lista) > 0: #se a lista tiver um número de itens maior que 0, será excluído o ')', pois ele fechou um '('
            lista.pop()
        else:
            lista.append(')') #senão ela irá incluir o ')' na lista
if len(lista) == 0: #se no final a lista tiver o tamanho de 0, ou seja, todos '(' foram fechados, a expressão é valida
    print('Expressão válida')
else: #senão será inválida
    print('Expressão inválida')
