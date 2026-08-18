numeros = []
continuar = 'S'
quantidade = 0
soma = 0
while continuar in 'Ss':
    numero = int(input('Digite um numero: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    numeros.append(numero)
    quantidade += 1
    soma += numero
    media = soma / quantidade
if numeros:
    print('Voce digitou {} numeros, e a media deles foi de {:.2f} '.format(quantidade, media))
    print('O maior numero é o {} e o menor é o {} '.format(max(numeros), min(numeros)))
else:
    print('Nenhum número foi digitado ')