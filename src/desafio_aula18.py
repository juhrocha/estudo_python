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




