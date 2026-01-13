# Declaração de classe

class MinhaClasse:
    # Metodo construtor
    def __init__(self):
        #Atríbutos de instância
        self.nome = '' #self é um nome genérico que posteriormente pode ser substituído na declaração dos objetos, assim ele saberá a quem atríbuir os métodos
        self.idade = 0

    #Métodos
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é aluno de Python e tem {self.idade} anos."

#Declaração de objeto
aluno1 = MinhaClasse() # Chamada inicial da função
aluno1.nome = 'Juliana' #Sem parênteses = atríbuto
aluno1.idade = 32
aluno1.aniversario()
print(aluno1.mensagem()) # Com parênteses = metodo
