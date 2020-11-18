# #Exercício 70 - Curso em vídeo
total_valor = contador_maior = menor_valor = contador = 0
nome_produto = ''
while True:
    produto=str(input('Nome do produto comprado: '))
    valor=float(input('Valor do produto: R$ '))
    continuar=str(input('Comprou algo mais? [S/N] ')).lower().strip()[0]
    total_valor+=valor
    contador+=1
    if valor >= 1000:
        contador_maior+=1
    if contador == 1:
        menor_valor=valor
        nome_produto = ''
    else:
        if valor < menor_valor:
            menor_valor = valor
            nome_produto = ''
    if continuar == 'n':
        break
print(f'''Valor total da compra: R${total_valor:.2f};
Produtos acima de R$1K: {contador_maior};
O produto mais barato custou: R${menor_valor:.2f} e foi {produto}''')
