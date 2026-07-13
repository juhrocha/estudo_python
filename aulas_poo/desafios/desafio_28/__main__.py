from classe_Termostato import Termostato
from rich import print, inspect

def main():
    t1 = Termostato()
    print(f'{t1.temperatura}')
    print(t1.ftemperatura)
    t1.temperatura = 20.5
    print(t1.ftemperatura)
    inspect(t1, private=True)

if __name__ == "__main__":
    main()