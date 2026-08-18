while True:
    tabuada = int(input('De qual numero voce quer ver a tabuada?? '))
    if tabuada < 0:
        break
    print('_' * 50)
    for i in range(1, 11):
        resultado = tabuada * i
        print(f'{tabuada} x {i} = {resultado}')
    print('_' * 50)
print('PROGRAMA FINALIZADO. NÚMEROS NEGATIVOS SÃO INVÁLIDADOS.')