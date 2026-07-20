from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O valor do SENO é {seno:.2f}\nO valor do COSSENO é {cosseno:.2f}\nO valor da TANGENTE é {tangente:.2f}')