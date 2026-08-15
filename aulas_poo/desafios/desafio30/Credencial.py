#Efetuado junto com o Guanabara
from hashlib import sha3_256

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha3_256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha inválida!')


    def validar(self, chave):
        usuario = sha3_256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            print('Senha não confere!')
            return False