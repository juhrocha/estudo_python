lista = ['banana', 'maça', 'pera']
print(list(enumerate(lista)))

for c, item in enumerate(lista):
    print(c, item)

for c, item in enumerate('Olá Mundo'):
    print(c, item)
