opcao = 'S'
cont = cont2 = cont3 = 0
while 'S' in opcao: 
    print('-'*40)
    print('CADASTRE UMA PESSOA')
    print('-'*40)
    idade = int(input('Idade: '))
    if idade > 18:
        cont += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        cont2 += 1
    elif sexo == 'F' and idade < 20:
        cont3 +=1
    print('-'*40)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Total de pessoas com mais de 18 anos: {}'.format(cont))
print('Ao todo temos {} homens cadastrados'.format(cont2))
print('E temos {} mulheres com menos de 20 anos'.format(cont3))