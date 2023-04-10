# Expressão regular = RegEx
import re
# texto = 'No momento estou ouvindo Somebody Told Me, da banda The Killers '
# """findall retorna em forma de lista a str encontrada"""
# resultado = re.findall(r'o', texto)
# print(resultado)
#
# """slipt retorna em forma de lista o resultado daquilo que você deseja retirar da expressão"""
# resultado = re.split(r'o', texto)
# print(resultado)
#
# """sub substitui uma informação por outra na expressão"""
# resultado = re.sub(r'Somebody Told Me, da banda The Killers ', 'Fátima, da banda Capital Inicial', texto)
# print(resultado)
#
# """operadores somados as funções executam diferentes resultados"""
# resultado = re.findall(r'\w*', texto)
# resultado = re.findall(r'o\w*', texto)
# print(resultado)


texto2 = 'O vídeo de Memórias (Pitty) foi postado há 08 anos'
# resultado = re.findall(r'\D+', texto2)
# resultado = re.sub(r'\D', '3', texto2)
resultado = re.sub(r'\S', '2', texto2)
print(resultado)
