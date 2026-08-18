print('GERADOR DE PA')
print('-' * 20)
termo1 = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
numero = termo1
c = 1
termos = 0
mais = 10
while mais != 0:
    termos = termos + mais
    while c <= termos:
        print('{} → '.format(termo1), end='')
        termo1 += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais voce quer ver?? '))
print('O programa finalizou com {} termos visualizados. '.format(termos))