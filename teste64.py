num = int(input('Digite um número[999 para parar]: '))
valores = 0
soma = 0
while num != 999:
    valores += 1
    soma = soma + num
    num = int(input('Digite um número[999 para parar]: '))
print('Voce digitou {} números, e a soma deles é {} '.format(valores, soma))
