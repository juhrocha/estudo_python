from aula_10_modulos import Aluno, Professor, Funcionario

a1 = Aluno('José', 10, 'Matemática', 'T01')
a1.fazer_aniversario()
a1.fazer_matricula()
print(f'A idade de {a1.nome} é {a1.idade} anos')

p1 = Professor('Pedro', 30, 'Matemática', 'T01')
p1.estudar()
print(f'A idade do prof. {p1.nome} é {p1.idade} anos')

f1 = Funcionario('Alana', 32, 'Secretária', 'Administração')
f1.estudar()
f1.fazer_aniversario()
print(f'A funcionária {f1.nome} trabalha no setor de {f1.setor} e tem {f1.idade}')

