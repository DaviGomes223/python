from math import hypot
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
print(f'O comprimento da hipotenusa é {hypot(co, ca):.2f}')