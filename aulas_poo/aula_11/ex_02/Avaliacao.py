class Avaliacao:
    def __init__(self, nome = '', disciplina = '', nota = 10):
        self.nome = nome #público
        self._disciplina = disciplina #protegido
        self.__nota = nota #privado

    #Métodos acessores
    def get_nota(self): #Metodo Getter
        return self.__nota

    def set_nota(self, valor): #Metodo Setter, por aceitar qlq coisa é necessário fazer algumas validações
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print('Informe uma nota válida!')