valor_casa = float(input('Qual o valor do imóvel que deseja comprar? R$ '))
salario = float(input('Qual o valor de seu salário? R$ '))
anos = int(input('Em quantos anos deseja quitar a casa? '))
minimo = salario*30/100
prestacao = (valor_casa/anos)/12
if prestacao <= minimo:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')