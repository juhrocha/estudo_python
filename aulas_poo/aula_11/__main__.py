from aulas_poo import aula_11
from aulas_poo.aula_11 import continuacao_aula_08

def main ():
    c1 = continuacao_aula_08.ContaBancaria(213, "João", 5000)
    c1.deposito(500)
    c1._titular = 'Pedro' #Python permite, mas lembrar de "Adultos consentindo"
    c1.__saldo = 0 #Neste caso ele não altera o valor do saldo, na vdd ele cria um outro atríbuto
    c1._ContaBancaria__saldo = 0 #Deste modo ele altera o valor do atríbuto, mas novamente não é recomendado
    print(c1)

if __name__ == "__main__":
    main()