numero=1
par=0
impar=0
while numero != 9:
    numero=int(input('Digite um número: '))
    if numero %2==0:
        par+=1
    else:
        impar+=1
print('Acabou')
print('Tivemos um total de {} números pares e {} números ímpares'.format(par,impar))


resposta = 's'
while resposta == 's':
    numero=int(input('Digite um valor: '))
    resposta=str(input('Você deseja continuar? S/N: ').lower())
print('FIM')