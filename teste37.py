num = int(input('Digite um numero inteiro: '))
binario = bin(num)
oct = oct(num)
hex = hex(num)
print('Escolha uma das bases de conversão: ')
print('[ 1 ] converter para BINÁRIO ')
print('[ 2 ] converter para OCTAL ')
print('[ 3 ] converter para HEXADECIMAL: ')
num2 = int(input('Sua opção: '))
if num2 == 1:
    print('{} convertido em BINÁRIO é {}'.format(num, binario[2:]))
elif num2 == 2:
    print('{} convertido em OCTAL é {}'.format(num, oct[2:]))
elif num2 == 3:
    print('{} covertido para HEXADECIMAL é {}'.format(num, hex[2:]))