"""" Classes servem para 'juntar' variáveis (atributos) e funções (metódos) dentro de um único lugar, o ato de 'juntar
essas informações é chamada de instâncias. Para usá-la você deve usar a palavra class seguida do nome dessa classe
(o nome deve possui a primeira letra em caixa alta.
Para iniciar a construção de uma classe é necessário criar primeiramente uma função inicial, definida como:
'def __init__(self):' """

class Pessoa():
    def __init__(self):
        self.nome = 'Juliana'
        self.nascimento = 1993
        self.ouvindo = 'QOTSA'
        print('CRIAÇÃO')

    def printar(self):
        print(f'Criei a instância da pessoa: {self.nome, self.nascimento, self.ouvindo}')


# # essa ação atribui a variável (atributo) a classe
pessoa1 = Pessoa()
# # após atribuir a variável a classe, é possível executar metódos (funções) de dentro da classe
# pessoa1.printar()
# # ou chamar uma atribuição (varíavel) em particular
# print(pessoa1.ouvindo)


# Classe com atribuição ao longo do código
# class Person:
#     def __init__(self, nome, nascimento):
#         self.nome = nome
#         self.nascimento = nascimento
#         print('CRIADO')
#
#     def impresso(self, nome, nascimento):
#         print(f'Você informou: nome {nome} e {nascimento}')
#
#
# person1 = Person('Juliana', '1993')
# person1.impresso('Juliana', 1993)
# print(person1.nome)

# retorna, em boleano, se o atributo possui ou não valor
print(hasattr(pessoa1, 'nome'))
# atualiza o registro de um atributo
setattr(pessoa1, 'nome', 'Reinaldo')
pessoa1.printar()
# retorna o registro identificado no atributo
print(getattr(pessoa1, 'nascimento'))
# deleta o registro identificado no atributo
delattr(pessoa1, 'ouvindo')
# erro ao printar proposital pela exclusão anterior
pessoa1.printar()




