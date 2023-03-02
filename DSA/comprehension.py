#LIST COMPREHENSION
# lista_numeros = [x for x in range(10)]
# print(lista_numeros)

#lista_numeros = [x for x in range(10) if x % 2 == 0]
#print(lista_numeros)

# frutas = ['maça', 'banana', 'pera', 'uva', 'kiwi', 'melancia', 'pitaya']
# frutas_3 = [x for x in frutas if 'n' in x]
# print(frutas_3)

#DICT COMPREHENSION
alunos = {'Bob': 10, 'May': 7, 'Rozy': 5, 'Van': 2, 'And': 0 }
status_alunos = {key: ('Aprovado' if value > 6 else 'Reprovado') for (key, value) in alunos.items()}
print(status_alunos)





