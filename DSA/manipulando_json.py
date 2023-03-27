import json
dict_json = {'nome': 'Guido', 'linguagem': 'Python',
             'similar': ['c', 'lisp'],
             'users': 100000}
# for key, value in dict_json.items():
#     print(key, value)

with open('/home/juliana/Documentos/dict_json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_json))

with open('/home/juliana/Documentos/dict_json', 'r') as file:
    texto = file.read()
    print(texto)

