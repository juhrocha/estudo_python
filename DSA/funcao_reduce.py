from functools import reduce
#list = [1, 2, 3, 4, 5]

#def soma(a, b):
#    return a + b


#reducao = reduce(soma, list)
#print(reducao)

#USANDO LAMBDA
#todo: refazer o código
list = [1, 2, 3, 4, 5, 6]
par = lambda x, false = 1: x if x % 2 == 0 else false
reducao = reduce(par, list)
print(reducao)
