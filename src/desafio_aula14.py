#Exercício 57 - Curso em vídeo - REFAZER
genero=str(input('Qual o seu gênero? [M/F]: ')).strip().upper()
while genero != 'M' or 'F':
    sexo=str(input('Gênero errado, tente novamente. Qual o seu gênero? [M/F]: ')).strip().upper()
print('Correto, pode prosseguir.')