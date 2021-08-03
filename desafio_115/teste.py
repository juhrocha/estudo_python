from desafio_115 import desafio115

while True:
    resposta = desafio115.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema')
        break
    else:
        print('Digite uma opção válida!')

