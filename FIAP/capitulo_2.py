#  Início do curso FIAP
print('Oi pessoal!')

# Capitulo 2
nome = 'Humberto Delgado'
empresa = 'FIAP'
qtde_funcionarios = 500
mediaMensalidade = 856.50
print(f'Olá meu nome é {nome} e trabalho na empresa {empresa}. Seja bem vindo!')
print(f'Minha empresa possui {qtde_funcionarios} funcionários e tem uma média de mensal de R$ {mediaMensalidade:.2f} '
      f'de cada um de seus alunos')

# Agora com input:
nome = str(input('Digite o nome de um funcionário: '))
empresa = str(input('Digite a empresa para que ele trabalha: '))
qtda_funcionarios = int(input('Quantos funcionários a empresa possui?: '))
media_mensalidade = float(input('Qual a média de salários da instituição?: '))
print(f'Olá me chamo {nome} e trabalho na empresa {empresa}.')
print(f'Minha empresa possui {qtda_funcionarios} funcionários e a média salarial é de R${media_mensalidade:.2f}')
print('*'*10)
print('Verificando o tipo de dado')
print('*'*10)
print('A variável nome é: ', type(nome))
print('A variável empresa é: ', type(empresa))
print('A variavel qtda_funcionarios é: ', type(qtda_funcionarios))
print('E a variavel media_mensalidade é: ', type(media_mensalidade))

# If, Elif, Else
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
if idade >= 65:
    print(f'{nome} você possui atendimento prioritário.')
else:
    print(f'{nome}, seu atendimento não é prioritário.')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
doenca = str(input('Possui doença contagiosa? [S/N] ')).upper().strip()
if idade >= 65 and doenca == 'S':
    print('Paciente de emergência, deve dirigir-se a sala A')
elif idade >=65 and doenca == 'N':
    print('Seu atendimento é prioritário, vá até a triagem preferencial')
elif idade < 65 and doenca == 'S':
    print('Paciente com risco de contagio, deve dirigir-se a sala B')
elif idade < 65 and doenca == 'N':
    print('Aguarde ser chamado para triagem')

# While
while True:
    idade = int(input('Digite sua idade: '))
    if idade == 50:
        break

# For
tabuada = int(input('Digite o número que deseja saber a tabuada: '))
print(f'Tabuada de {tabuada}: ')
for numero in range (1,11):
    print(f'{tabuada} x {numero} = {(tabuada*numero)}')
