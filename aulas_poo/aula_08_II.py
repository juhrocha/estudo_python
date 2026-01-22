class ContaBancaria:
    """
Cria uma conta bancária e permite saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada para o usuário {self.titular}')

    def __str__(self):
        return f'A conta {self.id} do titular {self.titular} tem R${self.saldo:.2f} de saldo'

    def deposito(self, valor): #self obrigatório nos metodos
        self.saldo += valor
        print(f'Depósito recebido, saldo atualizado: R${self.saldo:.2f}')

    def saque(self, valor):
        if valor > self.saldo:
            print('Saque não autorizado por saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque realizado, saldo atualizado: R${self.saldo:.2f}')

a1 = ContaBancaria(1, 'Juliana', 19)
a1.deposito(10)
a1.saque(500)
print(a1)