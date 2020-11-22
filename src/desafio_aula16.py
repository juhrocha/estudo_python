# Exercício 72 - Curso em vídeo
contagem=('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero=int(input('Digite um número ente 0 e 10: '))
    if numero <=10:
        break
print(f'Você digitou o número {contagem[numero]}')

# Exercício 73 - Curso em vídeo
times=('Flamengo','Atlético - MG','Internacional','SPFC','Palmeiras',
'Santos', 'Grêmio','Fluminense','Atlético-PR','Bahia','Bragantino',
'Sport','Fortaleza','Corinthians','Ceará','Atlético-GO','Vasco',
'Coritiba','Botafogo','Goiás')
print(times[0:5])
print(times[-4:])
print(sorted(times))
print(len('SPFC'))

# Exercício 74 - Curso em vídeo
from random import randint
aleatorio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram: {aleatorio}')
print(f'O maior valor sorteado foi: {max(aleatorio)}')
print(f'E o menor valor sorteado foi: {min(aleatorio)}')

# Exercício 75 - Curso em vídeo
valor=(int(input('Digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('Digite o último valor: ')))
print(f'Os valores digitados foram: {valor}')
print(f'O número 9 aparece: {valor.count(9)} vez(es) nessa lista')
if 3 in valor:
    print(f'O número 3 foi digitado na posição: {valor.index(3)+1}')
else:
    print('O número 3 não foi digitado.')
print('O(s) número(s) par(es) digitado(s) foi(ram): ',end='')
for numero in valor:
    if numero %2==0:
        print(numero , end='  ')

