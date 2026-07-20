nome = str(input('Qual é o seu nome completo? ')).upper().strip()
nome1 = nome.split()
print('Seu nome tem Silva? {}'.format('SILVA' in nome1))