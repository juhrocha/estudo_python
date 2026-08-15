from Credencial import Credencial

def main():
    c = Credencial()
    c.senha = 'BonJovi123'
    print(c.senha)
    c.validar('Teste123')

if __name__ == '__main__':
    main()