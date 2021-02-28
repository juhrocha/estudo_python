lanche=['pizza','pão','suco','café']
print(lanche)
lanche[2]='limão'
print(lanche)
lanche.append('refrigerante')
print(lanche)
lanche.insert(1,'queijo')
print(lanche)
del lanche [0]
print(lanche)
lanche.remove('café')
print(lanche) 

valor=list(range(4,11))
print(valor)

valor=[2,9,10,6,8,7,1,0]
print(valor)
valor.sort()
print(valor)
valor.append(3)
print(valor)
valor.sort(reverse=True)
print(valor)
if 3 in valor:
    valor.remove(3)
    print(valor)
else:
    print('A lista não contém o número 3')


nome=[]
nome.append('Maria')
nome.append('José')
nome.append('Mel')
#for name in nome:
#    print(f'O nome dele é {name}')
for count, name in enumerate(nome):
    print(f'Na posição {count} está {name},')
print('Eles chegaram!')

valores=list()
for contador in range (0,10):
    valores.append(int(input('Digite um número: ')))
print(valores)