# Exercício 94 - Curso em vídeo
pessoas_lista = []
pessoas_dicionario = {}
soma = media = 0
while True:
    pessoas_dicionario.clear()
    pessoas_dicionario['nome'] = str(input('Nome: '))
    pessoas_dicionario['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    while True:
        if pessoas_dicionario['sexo'] in 'MF':
            break
        else:
            print('ERRO! DIGITE SOMENTE M OU F')
            pessoas_dicionario['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    pessoas_dicionario['idade'] = int(input('Idade: '))
    soma+= pessoas_dicionario['idade']
    pessoas_lista.append(pessoas_dicionario.copy())
    resposta = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    while True:
        if resposta in 'SN':
            break
        else:
            print('ERRO! DIGITE SOMENTE S OU N')
            resposta = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(pessoas_lista)} pessoas nesta lista')
media = soma / len(pessoas_lista)
print(f'A média de idade entre as pessoas cadastradas é de {media:.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for mulher in pessoas_lista:
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]}')
print('A pessoa com idade acima da média é: ', end='')
for velho in pessoas_lista:
    if velho['idade'] > media:
        print(f'{velho["nome"]} com {velho["idade"]} anos')


# Exercício 95 - Curso em vídeo
