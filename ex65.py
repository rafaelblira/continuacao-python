n = int(input('Digite um número: '))
opcao = str(input('Quer continuar? [S/N)')).strip().upper()
cont = 1
soma = 0
total = 0
media = 0
maior = n
menor = n
num = n
while opcao != 'N':
    cont += 1
    nun = int(input('Digite um número: '))
    total += nun
    opcao = str(input('Quer continuar? [S/N)')).strip().upper()
    if nun > maior:
        maior = nun
    if num < menor:
        menor = num
soma = total + n
media = soma / cont
print('Você digitou {} números e a média foi {}.'.format(cont, media ))
print('O maior número digitado foi {} e o menor número foi {}.'.format(maior, menor))
