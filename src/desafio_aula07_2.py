from random import choice
aluno1=str(input('Nome do primeiro aluno: '))
aluno2=str(input('Nome do segundo aluno: '))
aluno3=str(input('Nome do terceiro aluno: '))
aluno4=str(input('Nome do quarto aluno: '))
lista=[aluno1,aluno2,aluno3,aluno4]
escolhido=choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))


import random
aluno5=str(input('Nome do aluno 1: '))
aluno6=str(input('Nome do aluno 2: '))
aluno7=str(input('Nome do aluno 3: '))
aluno8=str(input('Nome do aluno 4: '))
lista=[aluno5,aluno6,aluno7,aluno8]
random.shuffle(lista)
print('A ordem de apresentação dos alunos será {}'.format(lista))



























