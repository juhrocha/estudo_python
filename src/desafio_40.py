nascimento = int(input('Qual o ano de seu nascimento? '))
idade_minima = 18
alistamento = 2020 - nascimento
if alistamento < idade_minima:
    print('Ainda não é o momento para você se alistar ao serviço militar.')
    print('Faltam {} anos para você se alistar'.format(idade_minima-alistamento))
elif alistamento > idade_minima:
    print('Já passou do seu prazo de alistamento, procure o Ministério da Defesa!')
    print('Já passaram {} anos do período de alistamento'.format(alistamento-idade_minima))
else:
    print('É hora de você se alistar! Corra!')

from datetime import date
atual=date.today().year
nascimento = int(input('Qual o ano de seu nascimento? '))
idade = atual - nascimento
if idade == 18:
    print('É hora de você se alistar! Corra!')
elif idade < 18:
    print('Ainda não é o momento para você se alistar ao serviço militar.')
    saldo = 18 - idade
    print('Ainda faltam {} anos para você se alistar'.format(saldo))
else:
    print('Já passou do seu prazo de alistamento, procure o Ministério da Defesa!')
    saldo2= idade - 18
    print(' Você deveria ter se alistado há {} anos'.format(saldo2))