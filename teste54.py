from datetime import date

contador = 0
somamaior = 0
somamenor = 0
anoatual = date.today().year
for contador in range(1, 8):
    nascimento = int(input('Em que ano a {} pessoa nasceu? '.format(contador)))
    idade = anoatual - nascimento
    if idade >= 21:
        somamaior += 1
    else:
        somamenor += 1
print('Temos {} pessoas NA MAIORIDADE'.format(somamaior))
print('Temos {} pessoas MENORES DE IDADE'.format(somamenor))