print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
while True:
    valor = int(input('Que valor você quer sacar? '))
    cinquenta = valor // 50
    if cinquenta != 0:
        print('Total de {} cédulas de R$50'.format(cinquenta))
    resto = valor - (cinquenta * 50)
    vinte = resto // 20
    if vinte != 0:
        print('Total de {} cédulas de R$20'.format(vinte))
    resto2 = resto - (vinte * 20)
    dez = resto2 // 10
    if dez != 0:
        print('Total de {} cédulas de R$10'.format(dez))
    resto3 = resto2 - (dez * 10)
    cinco = resto3 // 5
    if cinco != 0:
        print('Total de {} cedulas de R$5'.format(cinco))
    resto4 = resto3 - (cinco * 5)
    if resto4 != 0:
        print('Total de {} cédulas de R$1'.format(resto4))
    print('\033[33m-=-\033[m'*21)
    print('\033[35mVolte sempre ao BANCO CEV! Tenha um bom dia!')
    break