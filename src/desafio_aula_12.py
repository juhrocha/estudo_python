# Exercício 36 - Curso em vídeo
valor_casa=float(input('Qual o valor da casa que deseja comprar? R$ '))
salario=float(input('Quanto você recebe por mês? R$ '))
anos=int(input('Em quantos anos você pretende pagar a casa? '))
mes=anos*12
prestacao=valor_casa/mes
porcentagem_salario=salario*0.3
if prestacao >= porcentagem_salario :
   print('Lamento, não conseguiremos aprovar o financiamento :(')
   print ('Com o seu salário de R${:.2f} você deve pagar prestações de até R${:.2f}'.format(salario, porcentagem_salario))
elif prestacao < porcentagem_salario :
    print('Parabéns, conseguiremos aprovar o seu financiamento :)')

# Exercício 37 - Curso em vídeo
numero=int(input('Digite um número inteiro: '))
print('''Escolha uma das seguintes opções: 
[1] converter em BINÁRIO
[2] converter em OCTAL
[3] converter em HEXADECIMAL''')
opcao= int(input('Qual opção desejada? '))
if opcao == 1:
    print('O número {} convertido em BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('O número {} convertido em OCTAL é igual a {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('O número {} convertido em HEXADECIMAL é igual a {}'.format (numero, hex(numero)))
else:
    print('OPÇÃO INVÁLIDA')
print('FIM')