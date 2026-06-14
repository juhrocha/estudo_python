import classe_transporte

def main():
    distancia = 10

    entrega1 = classe_transporte.Moto(distancia)
    entrega1.calc_frete()

    entrega2 = classe_transporte.Caminhao(distancia)
    entrega2.calc_frete()

    entrega3 = classe_transporte.Drone(distancia)
    entrega3.calc_frete()

if __name__ == "__main__":
    main()