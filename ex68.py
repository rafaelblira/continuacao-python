from random import randint
cont = 0
while True:
    print('-='*30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*30)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar [P/I] ').strip().upper())[0]
    print('Você jogou {} e o computador {}. Total de {}'.format(jogador, computador, total))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            cont += 1
        else:   
            print('Você perdeu')
            break
    print('Vamos jogar novamente ...')
print('Game Over! Você venceu {} vezes.'.format(cont))
    
    