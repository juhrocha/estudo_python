import moeda
valor = float(input('Digite um valor: R$ '))
print(f'O dobro do valor digitado é {moeda.moeda(moeda.dobro(valor))}')
print(f'Já {moeda.moeda(valor)} reduzido em 5% é igual a {moeda.moeda(moeda.diminuir(valor, 5))}')

