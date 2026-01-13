# Exercício 84 - Curso em vídeo
pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    if resposta == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso cadastrado foi {maior}Kg',end=' ')
for person in pessoas:
    if person[1] == maior:
        print(f'de {person[0]}')
    elif person[1] == menor:
        print(f'Já o menor peso cadastrado foi {menor}Kg',end= ' ')
        print(f'de {person[0]}')

# Exercício 85 - Curso em vídeo
valor = [[], []]
numero = 0
for num in range (0,7):
    numero = (int(input(f'Digite {num+1}º valor:  ')))
    if numero % 2 ==0:
        valor[0].append(numero)
    else:
        valor[1].append(numero)
valor[0].sort()
print(f'Os números pares digitados são {valor[0]};')
valor[1].sort()
print(f'Os números ímpares digitados são {valor[1]}')

# Exercício 86 - Curso em vídeo
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]: '))
print('A matriz digitada foi:')
for line in range (0,3):
    for colun in range (0,3):
        print(f'[{matriz[line][colun]:^5}]',end=' ')
    print()

# Exercício 87 - Curso em vídeo
matriz = [[0,0,0],[0,0,0],[0,0,0]] #aqui eu já determino o conteúdo da lista, pois irei SUBSTITUI-LOS e não ADICIONAR novos elementos
soma_par = maior = soma_coluna = 0
for linha in range (0,3): #devo fazer um laço pra linha e outro pra coluna
    for coluna in range (0,3):
        matriz[linha][coluna]= int(input(f'Digite um valor para a posição [{linha}], [{coluna}]: ')) #aqui uso o indexador em matriz para determinar onde o valor inputado irá substituir
print('A matriz digitada foi: ')
for line in range (0,3): #o primeiro laço é para input de infos e o segundo é para visualização
    for colun in range (0,3):
        print(f'[{matriz[line][colun]:^5}]', end=' ')
        if matriz[line][colun] % 2 == 0:
            soma_par+=matriz[line][colun] #aqui somo o número [x,y] posição a cada vez que o valor inputado seja par
    print()
print(f'A soma dos números pares da matriz é igual a : {soma_par}')
for li in range (0,3):#um novo laço deve ser criado para a soma da terceira coluna
    soma_coluna += matriz[li][2] #a terceira coluna é fixa, desse modo o que altera é apenas a posição da linha
print(f'A soma dos números contidos na terceira coluna é igual a : {soma_coluna}')
for co in range (0,3): #um outro laço para a soma da segunda linha
    if co == 0: #uso um if para verificação do maior número. Aqui a segunda linha é fixa, alterando somente a posição da coluna
        matriz[1][co] = maior
    elif matriz[1][co] > maior:
        maior =  matriz[1][co]
print(f'O maior número da segunda linha da matriz é: {maior}')
