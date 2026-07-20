from random import randint   #IMPORTANDO O RADINT PARA RANDOMIZAR UM NUMERO 
num = int
print('-' * 50)
print('Vou pensar em um numero de 0 a 5, tenta adivinhar...')
print('-' * 50)
num = randint(0, 5)     #FAZ O COMPUTADOR PENSAR EM UM NUMERO ALEATORIO
num1 = int(input('Em que número pensei? '))     #USUARIO TENTA ADIVINHAR O NUMERO PENSADO
print('PROCESSANDO... ')
if num1 == num:
    print('Parabens! Voce acertou o numero!! ')
else:
    print('Nah! Voce errou o numero! ')