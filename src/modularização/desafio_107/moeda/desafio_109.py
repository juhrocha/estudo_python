import moeda_2
cash = float(input('Digite um valor: R$ '))
print(f'O dobro do valor digitado é {moeda_2.dobro(cash, True)}')
print(f'Já {moeda_2.moeda(cash)} reduzido em 5% é igual a {moeda_2.diminuir(cash, 5, True)}')
print(f'A metade dessa quantia é {moeda_2.metade(cash, True)}')
