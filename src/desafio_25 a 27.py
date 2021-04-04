#Exercício 25 - Curso em vídeo
nome=str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

#Exercício 26 - Curso em vídeo
frase=str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase' .format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {} da frase'.format(frase.find('a')))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')))

#Exercício 27 - Curso em vídeo
completo=str(input('Digite seu nome completo: ')).strip()
nomes=completo.split()
print('Olá muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomes[0]))
print('E seu último nome é {}'.format(nomes[-1]))

name=input('Digite seu nome ')
separado=n.split()
print(separado[-1])




