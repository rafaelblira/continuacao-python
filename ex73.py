resp = ' '
times = ('corinthians', 'palmeiras', 'santos', 'grêmio', 'cruzeiro', 'flamengo', 'vasco',
'chapecoense', 'atlético', 'botafogo', 'atlético-PR', 'bahia', 'são paulo', 'fluminense', 
'sport recife', 'ec vitória', 'coritiba', 'avaí', 'ponte preta', 'atlético-GO' )
print('Escolha uma das opções abaixo par exibir:')
print(' [A] Os 5 primeiros\n [B] Os últimos 4 colocados\n [C] Times em ordem alfabética\n [D] Em que posição está o Chapecoense\n [E] sair\n')
while resp in 'ABCDE ':
    resp = str(input('Digite a opção desejada: ')).strip().upper()[0]
    if resp == 'A':
        print(times[0:5])
        print('='*30)
    elif resp == 'B':
        print(times[16:20])
        print('='*30)
    elif resp == 'C':
        print(sorted(times))
        print('='*30)
    elif resp == 'D':
        print('O chapecoense está em {}º'.format(times.index('chapecoense')+1))
        print('='*30)
    elif resp == 'E':
        break
    else:
        print('Opção inválida, tente novamente.')