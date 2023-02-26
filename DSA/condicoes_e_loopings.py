#IF ELSE
# numero = int(input('Digite um número de 1 a 10: '))
# if numero in range (1, 11):
#     print(f'Você digitou o número {numero}')
# else:
#     print('Você digitou um valor diferente do solicitado!')

# #ELIF
# semana = input('Qual dia da semana é hoje? ').lower()
# if semana == 'sábado':
#     print('Ótimo, é final de semana!')
# elif semana == 'domingo':
#     print('Ótimo, é final de semana!')
# elif semana == 'sexta':
#     print('Sextoooou!')
# elif semana == 'segunda':
#     print('A semana acabou de começar :(')
# else:
#     print('Ainda falta um pouco para o fds!')

#TESTANDO ALGUNS OPERADORES
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for numero in lista_numeros:
#     if numero % 2 == 0:
#         print(f'O número {numero} é par')
#     elif numero >= 5:
#         print(f'Já o {numero} é maior que ou igual a 5')

# #LOOPING ANINHADOS
# from datetime import date
# nascimento = int(input('Qual o ano de seu nascimento? '))
# idade = date.today().year - nascimento
# if idade >= 18:
#     if idade >= 70:
#         print('Acho que você pode descansar o volante')
#     else:
#         print('Boa direção')
# else:
#     print('Lamento, você não pode digirir ainda')

#OPERADORES LÓGICOS
# numero = int(input('Digite um número: '))
# if (numero > 2) and (numero % 2 == 0):
#     print(f'A variável recebida {numero} está sendo impressa por conter condições verdadeiras')
# else:
#     print('A variavel recebida não está sendo impressa por conter condições falsas')

# numero = int(input('Digite um número: '))
# if (numero > 10) or (numero % 3 == 0):
#     print(f'A variável recebida {numero} está sendo impressa por conter condições verdadeiras')
# else:
#     print('A variavel recebida não está sendo impressa por conter condições falsas')

# numero = int(input('Digite um número: '))
# if not (numero > 10) and (numero % 2 == 0):
#     print(f'A variável recebida {numero} está sendo impressa por conter condições verdadeiras')
# else:
#     print('A variavel recebida não está sendo impressa por conter condições falsas')

# semana = input('Qual dia da semana é hoje? ').lower()
# if semana == 'sábado' or semana == 'domingo':
#     print('Ótimo, é final de semana!')
# elif semana == 'sexta':
#     print('Sextoooou!')
# elif semana == 'segunda':
#     print('A semana acabou de começar :(')
# else:
#     print('Ainda falta um pouco para o fds!')

# #WHILE
# while True:
#     resposta = str(input('Você deseja continuar o looping? [S/N] ')).upper()
#     if resposta == 'N':
#         break

#LOOPING ANINHADO
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
soma = 0

# for lista in [lista1, lista2]:
#     for numero in lista:
#         if numero % 2 == 0:
#             soma += numero
# print(soma)

# for elemento in lista1:
#     for elemento2 in lista2:
#         print(f'{elemento} + {elemento2}')
