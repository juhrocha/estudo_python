rs=float(input('Quantos reais você tem na carteira: R$'))
d=(rs*5.53)
print('Em sua carteira você tem R${:.2f}, convertido em dólar você possui {:.2f}'.format(rs,d))


p=float(input('Qual o preço do produto: R$'))
d=(p*5/100)
print('O produto com 5% de desconto saí: R${:.2f}'.format(p-d))

preço=float(input('Qual o preço do produto: R$'))
desconto=preço-(preço*5/100)
print('O produto com o desconto de 5% saí no valor de R${:.2f}'.format(desconto))

salario=float(input('Qual é o seu salário?: R$'))
aumento=salario+(salario*15/100)
print('Com um aumento de 15% seu salário agora é de: R${:.2f}'.format(aumento))
























