class Diario:
    def __init__(self):
        #Não esquecer das formas de encapsulamento
        self.__segredos = []
        self.__senha = 'BonJovi123'

    @property
    def escrever(self):
        return self.__segredos

    @escrever.setter
    def escrever(self, mensagem):
        self.__segredos.append(mensagem)

    #São duas funções escrever, sendo uma getter e outra setter. Caso eu utilizasse o property como getter e solicitasse
    #o append, não funcionaria

    def ler(self, senha = ''):
        self.senha = senha
        if senha != self.__senha:
            print('Senha incorreta! Você não pode ler o conteúdo!')
        else:
            print('Diário liberado!')
            for segredo in self.__segredos:
                print(f'- {segredo}')

#Resolução do Guanabara
#Ele não utilizou getter e setter como eu, mas ambas resoluções funcionaram, houve uso da biblioteca rich e do PermissionError