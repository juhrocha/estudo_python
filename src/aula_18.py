teste=[] # lista "zerada" e abaixo adc dois elementos
teste.append('Juliana')
teste.append(27)
testando=[] # nova lista e abaixo copio os elementos contidos na lista anterior
testando.append(teste[:])
print(teste) # nesses prints é possível perceber que ambas variaveis_compostas.py ficaram iguais
print(testando)
teste.append('Reinaldo') # aqui adc elementos à primeira lista
teste.append(28)
print(teste) # ao printar aqui é possível perceber que as variaveis_compostas.py mudaram, inclusive as posições contidas nelas
print(testando)
print(teste[0])
print(testando[0])

gal = [['Juliana', 27], ['Reinaldo', 28], ['Loki', 3], ['Rodolfo', 29]]
print(gal[1])
print(gal[0][1])
print(gal[2][1])
print(gal)
for pessoa in gal:
    print(f'Nome: {pessoa[0]}',end=', ')
    print(f'Idade: {pessoa[1]}')

pessoas=[] # aqui crio a lista principal e uma auxiliar
dados=[]
maior=menor=0
for contador in range(0,3): # crio um for para me auxiliar na inclusão de dados à lista
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:]) # aqui copio as informações da lista "dados" na minha lista principal
    dados.clear() # aqui excluo os dados da minha lista auxiliar para evitar conflito de informações
for person in pessoas:
    if person[1] >=21:
        maior+=1
    else:
        menor+=1
print(f'Nesse grupo de pessoas temos {maior} maior(es) de idade e {menor} menor(es) de idade')
