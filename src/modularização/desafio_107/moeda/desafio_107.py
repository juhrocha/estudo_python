import moeda
moeda1 = float(input('Digite um valor: R$ '))
print(f'A metade do valor de R$ {moeda1} é R$ {moeda.metade(moeda1)}')
print(f'O dobro de R$ {moeda1} é R$ {moeda.dobro(moeda1)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(moeda1, 10)}')
