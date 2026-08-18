from random import randint


print('-' * 30)
print('\tIMPAR OU PAR ')
print('-' * 30)
vitoria = 0

while True:
    valor = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = computador + valor
    valor2 = ' '
    while valor2 not in 'PI':
        valor2 = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
        print(f'O jogador jogou {valor}, e o computador jogou {computador}, total de {total}, ', end='')
        print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if valor2 == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            vitoria += 1
        else:
            print('GAME OVER!')
            break
    if valor2 == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            vitoria += 1
        else:
            print('GAME OVER')
            break
print(f'Voce venceu {vitoria} vezes! ')
