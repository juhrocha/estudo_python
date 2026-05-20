#Utilizando modularização e a função main

import classe_bebidaquente
def main():
    bebida = classe_bebidaquente.Cafe()
    bebida.preparar()

    bebida = classe_bebidaquente.Cha()
    bebida.preparar()

    bebida = classe_bebidaquente.Leite()
    bebida.preparar()

if __name__ == "__main__":
    main()