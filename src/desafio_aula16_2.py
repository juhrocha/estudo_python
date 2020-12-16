# Exercício 75 - Curso em vídeo - Fixação
numero = (int(input('Digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('Digite o último valor: ')))
print(f'Você digitou o número nove {numero.count(9)} vezes')
if 3 in numero:
    print(f'O número 3 está na posição {numero.index(3)+1}')
else:
    print('O número 3 não foi digitado.')
print('São pares os números: ',end='')
for valor in numero:
    if valor %2 == 0:
        print(f'{valor}', end=' ')

# Exercício 76 - Curso em vídeo
materiais = ('Lápis', 1.00, 'Caneta', 1.50, 'Borracha', 0.50, 'Estojo', 5.00)
for posicao in range (0, len(materiais)):
    if posicao %2 ==0:
        print(f'{materiais[posicao]:.<30}', end=' ')
    else:
        print(f'R${materiais[posicao]:>5.2f}')

# Exercício 77 - Curso em vídeo
tupla = 'Juliana', 'Reinaldo', 'Bruno', 'Renata'
for palavra in tupla:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')