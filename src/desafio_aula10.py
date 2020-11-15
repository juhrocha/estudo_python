#  Exercício 30 - Curso em vídeo
numero=int(input('Me diga um número qualquer: '))
resultado=numero%2
if resultado == 0:
    print('O número informado é \33[32mPAR\33[m')
else:
    print('O número informado é \33[33mIMPAR\33[m')

#  Exercício 32 - Curso em vídeo
ano=int(input('Informe o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} FOI BISSEXTO'.format(ano))
else:
    print('O ano de {} NÃO FOI BISSEXTO'.format(ano))

#  Exercício 33 - Curso em vídeo
numero1=int(input('Digite um número: '))
numero2=int(input('Digite mais um número: '))
numero3=int(input('Digite outro número: '))
menor=numero1
if numero2<numero1 and numero2<numero3:
    menor=numero2
if numero3<numero1 and numero3<numero2:
    menor=numero3
print('O menor valor digitado foi {}'.format(menor))
maior=numero1
if numero2>numero1 and numero2>numero3:
    maior=numero2
if numero3>numero1 and numero3>numero2:
    maior=numero3
print('O maior valor digitado foi {}'.format(maior))
