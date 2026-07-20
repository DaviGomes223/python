primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razao
for i in range(primeiro, decimo, razao):
    print('{} '.format(i), end='→ ')
print('ACABOU! ')
