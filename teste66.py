numero = int(input('Digite um numero(999 para parar): '))
soma = 0
valores = 0
while numero != 999:
    valores += 1
    soma += numero
    numero = int(input('Digite um numero(999 para parar): '))
    if numero == 999:
        break
print(f'A soma dos {valores} valores é {soma}! ')