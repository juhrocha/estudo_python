try:
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outro número inteiro: '))
except (ValueError, TypeError):
    novamente = int(input('Você não digitou um número inteiro. Tente novamente: '))
finally:
    print('Obrigada pela correção.')
