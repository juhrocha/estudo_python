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
    print(f'Que {animal[1]} fofo!') # aqui o print com [] dá o animal na posição 2
#    print(f'Que {bicho[2]} fofo!') # aqui o [] exibe a 2 posição do bicho
print('FIM')
