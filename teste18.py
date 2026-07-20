import math
angulo = float(input('Digite o valor do angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O valor do SENO é {seno:.2f}\nO valor do COSSENO é {cosseno:.2f}\nO valor da TANGENTE é {tangente:.2f}')