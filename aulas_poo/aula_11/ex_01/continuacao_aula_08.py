from rich import inspect

class ContaBancaria:
    """
Cria uma conta bancária e permite saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id #público (*)
        self._titular = nome #protegido (#)
        self.__saldo = saldo #privado (-)
        print(f'Conta {self.id} criada para o usuário {self._titular}')

    def __str__(self):
        return f'A conta {self.id} do _titular {self._titular} tem R${self.__saldo:.2f} de __saldo'

    def deposito(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito recebido, __saldo atualizado: R${self.__saldo:.2f}')

    def saque(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print('Saque não autorizado por __saldo insuficiente')
        else:
            self.__saldo -= valor
            print(f'Saque realizado, __saldo atualizado: R${self.__saldo:.2f}')
