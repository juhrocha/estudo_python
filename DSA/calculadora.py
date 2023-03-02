def calcular():
    opcao = int(input('Digite uma das opções acima: '))
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} - {num2} = {num1 + num2}')
    elif opcao == 3:
        print(f'{num1} * {num2} = {num1 + num2}')
    elif opcao == 4:
        print(f'{num1} / {num2} = {num1 + num2}')
    else:
        print('Opção digitada não localizada')

from time import sleep
print('**Calculadora Python**\n')
sleep(1)
print('Lista de opções\n'
                     '1- Soma\n'
                     '2 - Subtração\n'
                     '3 - Multiplicação\n'
                     '4 - Divisão\n')
sleep(1)
calcular()

