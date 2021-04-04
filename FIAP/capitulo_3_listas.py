# Listas simples
valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resposta = (str(input('Deseja continuar adc números à lista? [S/N] '))).upper().strip()
    if resposta == 'N':
        break
print(f'A lista digitada foi {valor}')

# Usando for para exibir a lista
for numero in valor:
    print(numero, end=' ')

# Listas compostas com múltiplos types
inventario = []
contador = soma_total = 0
while True:
    equipamento = [(str(input('Mobília: '))), (str(input('Possui defeito? [S/N] '))).upper().strip(),
                   (float(input('Valor de mercado: R$ ')))]
    inventario.append(equipamento)
    resposta = (str(input('Você deseja continuar? [S/N} '))).upper().strip()
    if equipamento[1] == 'S':
        contador += 1
    soma_total += equipamento[2]
    if resposta == 'N':
        break
print('As mobílias de seu inventário são: ', end='')
for elemento in inventario:
    print(elemento[0][:], end=', ')
print()
print(f'Há {contador} mobília(s) com defeito nesse inventário.')
print(f'O valor total desse inventário é de R$ {soma_total:.2f}.')
print(inventario)

# Lista númerica com a biblioteca time
from time import sleep
valores = []
while True:
    valores.append(int(input('Digite um valor para a lista: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break
sleep(3)
print(f'A soma dos valores digitados é {sum(valores)}')
sleep(3)
print(f'Foram digitados {len(valores)} números')
sleep(3)
print(f'O maior valor digitado foi {max(valores)}')
sleep(3)
print(f'E o menor número digitado foi {min(valores)}')
sleep(3)
print(f'Os números digitados foram: {valores}')

