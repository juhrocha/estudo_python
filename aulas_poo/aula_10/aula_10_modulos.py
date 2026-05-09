from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod #Fazendo isso, eu obrigo as subclasses a terem esse metodo
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # É necessário utilizar o super
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer matrícula')

    def estudar(self):
        print(f'O aluno {self.nome} está estudando para a prova de {self.curso}')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Prof. {self.nome} começou a dar aula')

    def estudar(self):
        print(f'O professor {self.nome} está estudando para se aprimorar na aula de {self.especialidade}')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} acabou de bater o ponto')

    def estudar(self):
        print(f'A funcionária {self.nome} se especializa para a área de {self.setor}')