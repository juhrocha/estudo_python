from rich import inspect
from aulas_poo.aula_09.aula_09_modulos import Aluno

a1 = Aluno('José', 10, 'Matemática', 'T01')
a1.fazer_matricula()
inspect(a1)