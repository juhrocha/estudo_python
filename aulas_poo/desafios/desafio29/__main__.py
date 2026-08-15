import Diario

def main():
    d = Diario.Diario()  #Não esquecer que se vc está trazendo o módulo inteiro no import que vc deve nomeá-lo ao chamar
                            #a classe. Exemplo: nome_do_modulo.nome_da_classe()
    d.escrever = 'Hello mundo'
    d.escrever = 'Isso é um teste'
    d.ler('456')

if __name__ == '__main__':
    main()