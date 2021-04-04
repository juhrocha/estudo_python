# #Exercício 65 - Curso em vídeo
resposta = 's'
media = soma = contador = maior = menor = 0
while resposta == 's':
    numero=int(input('Digite um número inteiro: '))
    resposta=str(input(' Você deseja continuar? [S/N] ')).lower().strip()
    soma+=numero
    contador+=1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
media=soma/contador
print('A média dos valores digitados é igual a {}'.format(media))
print('Destes o maior número é {} e o menor é {}'.format(maior,menor))


