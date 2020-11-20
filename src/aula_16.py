animal = ('cão', 'gato', 'ave', 'cobra')
print(animal[-3])
print(animal[0])
print(animal[0:])
print(animal[:2])
print(animal[1:3])
print(sorted(animal)) #sorted coloca o print em ordem alfabética
for bicho in animal:
#nesse caso não é necessário usar "in range xxx"
#OUTRA FORMA DE USO DO FOR:
#for bicho in range (0,len(animal)):
#   print(f'Que {animal[bicho]} fofo!)
    print(f'Que {bicho} fofo!')
print('FIM')