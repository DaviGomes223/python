c = 0
total = 0
num = int(input('Digite um número: '))
for c in range(1, num +1):
    if num % c == 0:
        print('\033[35m ',end='')
        total += 1
    else:
        print('\033[34m', end=' ')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes '.format(num, total))
if total == 2:
    print('O NUMERO É PRIMO! ')
else:
    print('O NUMERO NÃO É PRIMO! ')

