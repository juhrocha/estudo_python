from Avaliacao import Avaliacao
from rich import print, inspect

def main():
    a1 = Avaliacao('Juliana', 'Inglês', 10)
    print(a1.get_nota())
    a1.set_nota(1)
    inspect(a1, private=True) #sem o private, ele não exibe os dados privados

if __name__ == '__main__':
    main()