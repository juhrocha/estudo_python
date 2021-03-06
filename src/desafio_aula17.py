# Exercício 78 - Curso em Vídeo
valor_num=list()
maior = menor = 0
for valor in range (0,5):
    valor_num.append(int(input('Digite um valor: ')))
    if valor == 0:
        maior = menor = valor_num[valor]
    else:
        if valor_num[valor] > maior:
            maior = valor_num[valor]
        elif valor_num[valor] < menor:
            menor = valor_num[valor]
print(f'A sua lista de valores é {valor_num}')
print(f'O maior número digitado foi {maior} e o menor número foi {menor}')
for posição, indexador in enumerate(valor_num):
    if indexador == maior:
        print(f'O maior número está na posição {posição}')
    elif indexador == menor:
        print(f'O menor número está na posição {posição}')
#REFAZER