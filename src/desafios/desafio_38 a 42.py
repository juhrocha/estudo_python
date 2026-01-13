#Exercício 38 - Curso em vídeo
num1=int(input('Digite um número: '))
num2=int(input('Digite outro número: '))
if num2>num1:
   print('O maior número é {}'.format(num2))
elif num1>num2:
    print('O maior número é {}'.format(num1))
else:
    print('Os números são iguais')

#Exercício 39 - Curso em vídeo
nascimento=int(input('Qual o ano em que você nasceu? '))
from datetime import date
obrigatorio = date.today().year-nascimento
if obrigatorio < 18:
    print('Você não precisa se alistar no momento.')
elif obrigatorio == 18:
    print('Você deve se alistar esse ano!')
else:
    print('Você já passou de seu período de alistamento.')

#Exercício 39 - Curso em vídeo
nota1=float(input('Digite a primeira nota do aluno: '))
nota2=float(input('Digite a segunda nota do aluno: '))
media=(nota1+nota2)/2
if media < 5.0:
    print('O aluno foi REPROVADO')
elif media <= 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno foi APROVADO')

#  Exercício 42 - Curso em vídeo
print('*'*20)
print('Analisador de triângulos')
print('*'*20)
reta1=float(input('Primeiro segmento: '))
reta2=float(input('Segundo segmento: '))
reta3=float(input('Terceiro segmento: '))
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('Esses segmentos PODEM FORMAR um triângulo')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:  
    print('Esses segmentos NÃO PODEM FORMAR um triângulo')