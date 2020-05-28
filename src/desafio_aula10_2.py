salario=float(input('Qual seu salário? R$'))
if salario>=1250.0:
    aumento=salario+(salario*10/100)
    print('O valor de seu salário é R${:.2f} e com aumento será R${:.2f}'.format(salario,aumento))
else:
    aumento2=salario+(salario*15/100)
    print('O valor de seu salário é R${:.2f} e com aumento será de R${:.2f}'.format(salario,aumento2))


print('*'*20)
print('Analisador de triângulos')
print('*'*20)
reta1=float(input('Primeiro segmento: '))
reta2=float(input('Segundo segmento: '))
reta3=float(input('Terceiro segmento: '))
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('Esses segmentos \33[4mPODEM FORMAR\33[m um triângulo')
else:  
    print('Esses segmentos \33[4mNÃO PODEM FORMAR\33[m um triângulo')













