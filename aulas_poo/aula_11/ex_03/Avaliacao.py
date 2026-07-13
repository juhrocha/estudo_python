class Avaliacao:
    def __init__(self, nome = '', disciplina = '', nota = 10):
        self.nome = nome #público
        self._disciplina = disciplina #protegido
        self.__nota = nota #privado

    #Caminho - Atríbuto validável
    @property
    def nota(self): #Getter
        return self.__nota

    @nota.setter
    def nota(self, valor): #Setter
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print('Informe uma nota válida!')
