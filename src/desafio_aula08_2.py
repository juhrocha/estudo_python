nome=str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))


frase=str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase' .format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {} da frase'.format(frase.find('a')))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')))


completo=str(input('Digite seu nome completo: ')).strip()
nomes=completo.split()
print('Olá muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomes[0]))
print('E seu último nome é {}'.format(nomes[-1]))




