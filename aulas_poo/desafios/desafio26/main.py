import classe_funcionario

def main():

    funcionario1 = classe_funcionario.Horista("Reinaldo", 12, 200)
    funcionario1.calc_sal()
    funcionario1.analisar_sal()

    funcionario2 = classe_funcionario.Mensalista("Juliana", 9500)
    funcionario2.calc_sal()
    funcionario2.analisar_sal()

if __name__ == "__main__":
    main()