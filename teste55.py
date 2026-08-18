contador = 0
maior = 0
menor = 0
for i in range(1, 6):
    contador += 1
    peso = float(input('O peso da {} pessoa: '.format(contador)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso registrado foi {}'.format(maior))
print('O menor peso registrado foi {}'.format(menor))
