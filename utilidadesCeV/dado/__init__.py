def leiaDinheiro (mensagem):
    flag = False
    while flag is not True:
        valor = str(input(mensagem)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'ERRO! Digite um valor válido!')
        else:
            flag = True
            return float(valor)
