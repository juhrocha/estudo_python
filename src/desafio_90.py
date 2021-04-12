Exercício 90 - Curso em vídeo
dados_alunos = {}
dados_alunos['Nome'] = str(input('Digite o nome do aluno: '))
dados_alunos['Media'] = float(input('Digite a média do aluno: '))
if dados_alunos['Media'] == 5:
    dados_alunos['Situacao'] = 'Recuperação'
elif dados_alunos['Media'] > 5:
    dados_alunos['Situacao'] = 'Aprovado'
elif dados_alunos['Media'] < 5:
    dados_alunos['Situacao'] = 'Reprovado'
for key, value in dados_alunos.items():
    print(f'{key} é igual a {value}')

# Exercício 90 - Curso em vídeo
