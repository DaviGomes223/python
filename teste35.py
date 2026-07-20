print('-_-' * 9)
print('Analisador de Triângulos')
print('-_-' * 9)
r1 = float(input('Digite a Primeira reta: '))
r2 = float(input('Digite a Segunda reta: '))
r3 = float(input('Digite a Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos FORMAM um triangulo!! ')
else:
    print('Os segmentos NÃO FORMAM um triangulo!! ')