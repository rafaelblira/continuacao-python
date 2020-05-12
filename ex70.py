total = totmil = cont = menor = 0
barato = ' '
print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil +=1
    if cont == 1 or preco < menor:
        barato = produto
        menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1000,00'.format(totmil))
print('O produto mais barato foi {} que custa {:.2f}'.format(barato, menor))


