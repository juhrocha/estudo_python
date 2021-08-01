try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
# except:
#     print('Tivemos um erro :(')
# except Exception as erro:
#     print(f'Problema encontrado: {erro.__class__}')
except ZeroDivisionError:
    print('Não é possível efetuar uma divisão por 0.')
except (ValueError, TypeError):
    print('Erro nos tipos digitados.')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Obrigada.')
