#Exercício 72 - Curso em vídeo
contagem=('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero=int(input('Digite um número ente 0 e 10: '))
    if numero <=10:
        break
print(f'Você digitou o número {contagem[numero]}')