tempo=int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')

#Método não convencional
tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('FIM')


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+ nota2)/2
print ('A sua nota media e de {}'.format(media))
if media>=6.0:
    print('Sua media foi boa')
else:
    print('Sua media foi baixa')

