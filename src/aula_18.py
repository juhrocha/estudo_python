teste=[]
teste.append('Juliana')
teste.append(27)
testando=[]
testando.append(teste[:])
print(teste)
print(testando)
teste.append('Reinaldo')
teste.append(28)
print(teste)
print(testando)

gal=[['Juliana',27],['Reinaldo',28],['Loki',3],['Rodolfo',29]]
print(gal[1])
print(gal[0][1])
print(gal[2][1])
print(gal)
for pessoa in gal:
    print(f'Nome: {pessoa[0]}',end=', ')
    print(f'Idade: {pessoa[1]}')

pessoas=[]
dados=[]
maior=menor=0
for contador in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for person in pessoas:
    if person[1] >=21:
        maior+=1
    else:
        menor+=1
print(f'Nesse grupo de pessoas temos {maior} maior(es) de idade e {menor} menor(es) de idade')
