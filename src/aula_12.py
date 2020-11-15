nome=str(input('Qual é seu nome? '))
if nome == 'Juliana':
    print('Que belo nome!')
elif nome == 'Maria Eduarda' or nome =='Maria Luisa' or nome =='Enzo':
    print('Hmmm, não gostei do seu nome')
else:
    print('Gostei do seu nome!')
print('Prazer em te conhecer, {}'.format(nome))

idade=int(input('Quantos anos você tem? '))
if idade <= 18 :
    print('Nossa, como você é jovem!')
elif idade <= 60:
    print('Você já é um adulto!')
else:
    print('Você já é um idoso!')

