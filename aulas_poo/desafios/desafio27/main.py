from classe_RPG import *


def main():
    personagem1  = Guerreiro('Ragnar', 1500)
    personagem2 = Mago('Merlin', 1000)

    personagem1.atacar(personagem2, 200)
    personagem2.atacar(personagem1)
    personagem2.curar()

if __name__ == "__main__":
    main()