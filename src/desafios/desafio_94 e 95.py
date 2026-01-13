# Exercício 94 - Curso em vídeo
pessoas_lista = []
pessoas_dicionario = {}
soma = media = 0
while True:
    pessoas_dicionario.clear() # apaga o dicionário no inicio do laço, a fim de evitar erros
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
    while True: # laço para corrigir o usuário caso digite algo diferente de N OU S
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
for mulher in pessoas_lista: # laço para evidenciar as mulheres da lista
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]}')
print('A pessoa com idade acima da média é: ', end='')
for velho in pessoas_lista: # laço para evidenciar aqueles com idade acima da média
    if velho['idade'] > media:
        print(f'{velho["nome"]} com {velho["idade"]} anos')

# Exercício 95 - Curso em vídeo
dados_jogador = {} # dicionário para salvar o jogador do laço
lista_jogadores = [] # lista para salvar os dados de cada jogador
lista_gols =[] # lista para salvar todos os gols cadastrados
while True:
    dados_jogador.clear() # para evitar erros a lista de gols e dicionário é apagada a cada laço
    lista_gols.clear()
    dados_jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    for partida in range(0, partidas):
        lista_gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))
    dados_jogador['gols'] = lista_gols[:] # adiciono a chave "gols" ao dicionário e copio nela a lista de gols
    dados_jogador['total de gols'] = sum(dados_jogador['gols']) # somo a chave "gols" para criar a chave "total de gols
    lista_jogadores.append(dados_jogador.copy()) # adiciono os itens do dicionário a lista para no inicio do novo laço exclui-lo
    while True: # um laço para corrigir o usuário caso digite algo diferente de N ou S em sua resposta
        resposta = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if resposta in 'SN':
            break
        else:
            print('ERRO! Digite somente S OU N!!!')
    if resposta == 'N': # break no primeiro laço
        break
print('*'*50)
for key, value in enumerate(lista_jogadores): # faço dois laços para pegar os itens da lista com dicionário
    print(f'{key:>3}', end=' ') # aqui apenas determino a posição desejada
    for item in value.values(): # aqui determino o item de cada posição
        print(f'{str(item):>10}', end=' ')
    print()
print('*'*50)
while True: # laço para o levantamento do jogador desejado
    buscador = int(input('Aproveitamento -> Digite o código do jogador ou digite 99 para encerrar: ')) # o buscador é a posição desejada do jogador na lista
    if buscador == 99: # flag no laço
        break
    if buscador >=len(lista_jogadores): # caso o usuário digite um usuário que não está na lista dará erro
        print('ERRO! Não há o jogador indicado, tente novamente!!!')
    else:
        print(f'Levantamento de {lista_jogadores[buscador]["nome"]}: ')
        for index, gol in enumerate(lista_jogadores[buscador]["gols"]):
            print(f'Na partida {index+1} fez {gol} gol(s)')
