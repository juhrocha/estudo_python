# Interactive Help
help(print)
help(float)

# Docstring
def contador (inicio, fim, passo):
    """Faz uma contagem e mostra na tela
    :param inicio: inicío da contagem;
    :param fim: final da contagem;
    :param passo: passo da contagem;
    :return: sem retorno"""
    começo = inicio
    while começo <=fim:
        print(f'{começo}', end=' ')
        começo+=passo
    print('Fim!')


help(contador)

contador(1, 20, 5)

# Argumento/Parâmetro opcional
def soma(a, b, c=0):
    s = a + b + c
    print(f'A soma é {s}')


soma(1, 2)

# Escopo de Varíaveis
def teste ():
    n = 10
    x = 3 # escopo local
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')


n = 2 # escopo global
print(f'No programa principal n vale {n}')
# print(f'No programa principal x vale {x}')
teste()

# Retorno de valores
def soma(a, b=0, c=0):
    s = a + b + c
    # print(f'A soma é {s}')
    return s


resposta1 = (soma(1, 2, 3))
resposta2 = (soma(2, 2))
resposta3 = (soma(1))
print(f'As somas valem: {resposta1}, {resposta2} e {resposta3}')

