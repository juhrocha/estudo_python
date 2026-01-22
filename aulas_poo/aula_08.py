class MinhaClasse:
    """
Essa classe cria uma pessoa com nome e idade
Para criar uma pessoa use: variavel = MinhaClasse(nome, idade)
    """

    def __init__(self, nome = '', idade = 0): #Eu posso opcionalmente determinar um default, que neste caso são valores vazios
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self): #Dunder method, o metodo str retorna uma string legível, por isso não há a necessidade de criar uma função de exibição de mensagens
        return f"{self.nome} é aluno de Python e tem {self.idade} anos."

aluno1 = MinhaClasse('Juliana', 32)
aluno1.aniversario()
print(aluno1)


aluno2 = MinhaClasse('Mauro')
print(aluno2)


#print(MinhaClasse.__doc__) #Acesso a docstring da minha classe, chamado Dunder attribute
#print(aluno1.__dict__) #Dunder atributo
#print(aluno1.__getstate__()) #Dunder metodo, virão acompanhados de ()