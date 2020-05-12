soma = cont = 0
while True:
    nun = int(input('Digite um valor [999 para parar]: '))
    if nun == 999:
        break
    cont += 1
    soma += nun
print('A soma dos {} valores foi {}!'.format(cont, soma))