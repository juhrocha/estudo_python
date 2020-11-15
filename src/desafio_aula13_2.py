#Exercício 54 - Curso em vídeo
from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for maioridade in range (0,7):
    nascimento = int(input('Qual seu ano de nascimento: '))
    idade = atual - nascimento
    if idade < 21:
        total_menor+=1
    elif idade >= 21:
       total_maior+=1
print('Nessa lista temos: {} pessoas que que já são maiores de idade e {} pessoas que ainda não atingiram a maioridade.'.format(total_maior, total_menor))
   
#Exercício 56 - Curso em vídeo
soma_idade=0
media_idade=0
idade_homem_velho=0
nome_homem_velho=''
contador_mulher=0
for grupo in range (1,5):
    print('*** {} PESSOA ***'.format(grupo))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo: [M/F]: ')).strip().upper()
    soma_idade+=idade
    if grupo == 1 and sexo == 'M':
        idade_homem_velho=idade
        nome_homem_velho=nome
    if sexo == 'M' and idade > idade_homem_velho:
        idade_homem_velho=idade
        nome_homem_velho=nome
    if sexo == 'F' and idade < 20:
        contador_mulher+=1 
media_idade = soma_idade/4
print('Neste grupo: a média de todas as idades é de {:.2f}'.format(media_idade))
print('O homem mais velho é {} e tem {} anos'.format(nome_homem_velho,idade_homem_velho))
print('Temos {} mulheres com menos de 20 anos'.format(contador_mulher))
