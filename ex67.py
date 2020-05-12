while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    else:
        print('-'*30)
        for c in range(1, 11):
            tab = num * c
            print('{} x {} = {}\n'.format(num, c, tab))
        print('-'*30)
print('Programa encerrado, volte sempre!')
    