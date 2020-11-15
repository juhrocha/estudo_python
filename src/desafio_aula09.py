#  Exercício 29 - Curso em vídeo
velocidade=float(input('Qual a velocide de seu carro? KM: '))
if velocidade <=60.0:
    print('\33[32m Parabéns! Dirija com cuidado sempre.')
else:
    print('\33[35m MULTATO! Sua velocidade está acima da permitida nessa rodovia!')
    multa=(velocidade-60.0)*7.0
    print('Você será multado em R${:.2f}'.format(multa))


























